from functools import reduce
import operator
from typing import Optional
import strawberry
from strawberry.types import Info

from utilities.querysets import RestrictedQuerySet

from .filter_mixins import BaseFilterMixin


from django.db.models import Q


def parse_filter_name(field_name: str) -> tuple[str, str]:
    """Parse filter name into field path and operator"""
    # Skip our internal lookups
    if field_name.startswith('__'):
        return None, None

    parts = field_name.split('__')
    if len(parts) == 1 or parts[-1] not in FILTER_LOOKUPS:
        return field_name, 'exact'
    return '__'.join(parts[:-1]), parts[-1]


FILTER_LOOKUPS = {
    # Exact matches
    'exact': lambda f, v: Q(**{f: v}),
    'is_null': lambda f, v: Q(**{f'{f}__isnull': v}),
    'in_list': lambda f, v: Q(**{f'{f}__in': v}),
    'i_exact': lambda f, v: Q(**{f'{f}__iexact': v}),

    # Numeric comparisons
    'gt': lambda f, v: Q(**{f'{f}__gt': v}),
    'gte': lambda f, v: Q(**{f'{f}__gte': v}),
    'lt': lambda f, v: Q(**{f'{f}__lt': v}),
    'lte': lambda f, v: Q(**{f'{f}__lte': v}),
    'range': lambda f, v: Q(**{f'{f}__range': v}),

    # Text matches
    'contains': lambda f, v: Q(**{f'{f}__contains': v}),
    'i_contains': lambda f, v: Q(**{f'{f}__icontains': v}),
    'starts_with': lambda f, v: Q(**{f'{f}__startswith': v}),
    'i_starts_with': lambda f, v: Q(**{f'{f}__istartswith': v}),
    'ends_with': lambda f, v: Q(**{f'{f}__endswith': v}),
    'i_ends_with': lambda f, v: Q(**{f'{f}__iendswith': v}),
    'regex': lambda f, v: Q(**{f'{f}__regex': v}),
    'i_regex': lambda f, v: Q(**{f'{f}__iregex': v}),

    # Null checks
    'isnull': lambda f, v: Q(**{f'{f}__isnull': v}),

    # Date/time
    'year': lambda f, v: Q(**{f'{f}__year': v}),
    'month': lambda f, v: Q(**{f'{f}__month': v}),
    'day': lambda f, v: Q(**{f'{f}__day': v}),
    'week': lambda f, v: Q(**{f'{f}__week': v}),
    'week_day': lambda f, v: Q(**{f'{f}__week_day': v}),
    'quarter': lambda f, v: Q(**{f'{f}__quarter': v}),
    'time': lambda f, v: Q(**{f'{f}__time': v}),
    'hour': lambda f, v: Q(**{f'{f}__hour': v}),
    'minute': lambda f, v: Q(**{f'{f}__minute': v}),
    'second': lambda f, v: Q(**{f'{f}__second': v}),
    'date': lambda f, v: Q(**{f'{f}__date': v}),
}


def build_filter_q(filters, prefix: str = '') -> tuple[Q, set[str]]:
    q = Q()
    used_fields = set()

    for field_name, value in vars(filters).items():
        if value is strawberry.UNSET or value is None:
            continue

        # Skip special fields
        if field_name.startswith('__'):
            continue

        used_fields.add(field_name)
        full_field = f"{prefix}{field_name}" if prefix else field_name

        # Handle logical operators (AND, OR, NOT)
        if field_name in ('AND', 'OR', 'NOT'):
            items_q = []
            filter_items = value if isinstance(value, (list, tuple)) else [value]

            # First collect all the Q objects
            for filter_item in filter_items:
                item_q, item_fields = build_filter_q(filter_item, prefix)
                used_fields.update(item_fields)
                items_q.append(item_q)

            # Important change: Different handling based on operator
            if field_name == 'AND':
                q &= reduce(operator.and_, items_q, Q())
            elif field_name == 'OR':
                q |= reduce(operator.or_, items_q, Q())
            else:  # NOT
                q &= ~reduce(operator.and_, items_q, Q())
            continue

        # Handle filter operation objects (like {i_exact: "value"})
        current_q = Q()  # Create a separate Q object for this field
        if hasattr(value, '__dict__'):
            operations = vars(value)
            for op_name, op_value in operations.items():
                if op_value is not strawberry.UNSET and op_name in FILTER_LOOKUPS:
                    current_q &= FILTER_LOOKUPS[op_name](full_field, op_value)
        else:
            # Default exact match for direct values
            current_q = FILTER_LOOKUPS['exact'](full_field, value)

        # Add the field's conditions to the main Q object
        q &= current_q

    return q, used_fields


def list_resolver(
    info: Info,
    queryset: RestrictedQuerySet,
    filters: Optional[BaseFilterMixin] = strawberry.UNSET,
):
    """Enhanced resolver that handles custom fields, relationships, and complex filtering"""
    if filters and filters is not strawberry.UNSET:
        # Handle custom fields
        if len(getattr(filters, '__netbox_field_map__', [])):
            q_filter, used_fields = build_filter_q(filters)
            # Update q_filter.children with transformed field names
            updated_children = []
            for key, value in q_filter.children:
                for prefix, new_prefix in filters.__netbox_field_map__.items():
                    if key.startswith(prefix):
                        new_key = key.replace(prefix, new_prefix, 1)
                        updated_children.append((new_key, value))
                        setattr(filters, prefix, strawberry.UNSET)
                        break
                else:
                    updated_children.append((key, value))
            q_filter.children = updated_children
        else:
            q_filter, used_fields = build_filter_q(filters)

        if q_filter:
            queryset = queryset.filter(q_filter)

        # Clear all used fields so strawberry won't process them
        for field in used_fields:
            setattr(filters, field, strawberry.UNSET)

    return queryset.distinct()
