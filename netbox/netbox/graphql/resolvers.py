from functools import reduce
from importlib import import_module
import operator
from typing import Optional
import strawberry
from strawberry.types import Info

from utilities.querysets import RestrictedQuerySet

from .filter_mixins import BaseFilterMixin


from django.db.models import Q

from django.db.models import ForeignKey
from django.db.models.fields.related_descriptors import (
    ForwardManyToOneDescriptor,
    ManyToManyDescriptor,
    ReverseManyToOneDescriptor,
)


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


def get_relationship_map(model):
    """Build a mapping of field names to their relationship paths."""
    relationship_map = {}
    related_models = {}

    model_attrs = {name: attr for name, attr in model.__dict__.items()}

    # Get ForwardManyToOne relationships (ForeignKey)
    for name, attr in model_attrs.items():
        if isinstance(attr, ForwardManyToOneDescriptor):
            base_name = name.rstrip('_id')
            relationship_map[f'{base_name}_id'] = f'{base_name}__id'
            relationship_map[base_name] = base_name
            if hasattr(attr, 'field'):
                related_models[base_name] = attr.field.related_model

    # Get ManyToMany relationships
    for name, attr in model_attrs.items():
        if isinstance(attr, ManyToManyDescriptor):
            singular_name = name.rstrip('s')
            relationship_map[f'{singular_name}_id'] = f'{name}__id'
            relationship_map[singular_name] = name
            if hasattr(attr, 'field'):
                related_models[singular_name] = attr.field.related_model

    # Get ReverseOneToMany relationships
    for name, attr in model_attrs.items():
        if isinstance(attr, ReverseManyToOneDescriptor):
            singular_name = name.rstrip('s')
            relationship_map[f'{singular_name}_id'] = f'{name}__id'
            relationship_map[singular_name] = name
            if hasattr(attr, 'rel'):
                related_models[singular_name] = attr.rel.related_model

    return relationship_map, related_models


def get_field_filterset(model):
    """
    Get the filterset class for a model by importing it dynamically.
    Assumes filtersets follow the Netbox convention of being in a 'filtersets' module
    and named as ModelNameFilterSet
    """
    if not model:
        return None

    # Get the model's module path components
    module_path = model.__module__
    app_path = '.'.join(module_path.split('.')[:-1])  # Remove the last part (usually 'models')

    try:
        # Import the filtersets module from the same app
        filtersets_module = import_module(f'{app_path}.filtersets')

        # Construct the expected filterset class name
        filterset_name = f'{model.__name__}FilterSet'

        # Get the filterset class
        return getattr(filtersets_module, filterset_name, None)
    except (ImportError, AttributeError):
        return None


def build_filter_q(filters, prefix: str = '', model=None) -> tuple[Q, set[str]]:
    """Build Django Q objects from filter values with relationship mapping"""
    q = Q()
    used_fields = set()

    if model is None:
        model = filters.filterset._meta.model

    for field_name, value in vars(filters).items():
        if value is strawberry.UNSET or value is None:
            continue

        # Skip special fields
        if field_name.startswith('__'):
            continue

        used_fields.add(field_name)

        # Handle logical operators (AND, OR, NOT)
        if field_name in ('AND', 'OR', 'NOT'):
            items_q = []
            filter_items = value if isinstance(value, (list, tuple)) else [value]

            for filter_item in filter_items:
                item_q, item_fields = build_filter_q(filter_item, prefix, model)
                used_fields.update(item_fields)
                items_q.append(item_q)

            if field_name == 'AND':
                q &= reduce(operator.and_, items_q, Q())
            elif field_name == 'OR':
                q |= reduce(operator.or_, items_q, Q())
            else:  # NOT
                q &= ~reduce(operator.and_, items_q, Q())
            continue

        # Transform field path and handle nested filters
        if hasattr(value, '__dict__') and not any(op in FILTER_LOOKUPS for op in vars(value)):
            # Get the pluralized relationship name if it exists
            relationship_map, related_models = get_relationship_map(model)
            base_field = relationship_map.get(field_name, field_name)

            # Get the related model's filterset if it exists
            nested_model = related_models.get(field_name)
            nested_filterset = get_field_filterset(nested_model)

            # Build the path with the relationship name and append the nested field
            for nested_field, nested_value in vars(value).items():
                if nested_value is not strawberry.UNSET and nested_value is not None:
                    # If we have a filterset for this relationship, use its mappings
                    if nested_filterset and nested_model:
                        nested_map, _ = get_relationship_map(nested_model)
                        nested_field = nested_map.get(nested_field, nested_field)

                    field_path = f'{base_field}__{nested_field}'
                    if prefix:
                        field_path = f'{prefix}__{field_path}'

                    # Handle nested operations
                    if hasattr(nested_value, '__dict__'):
                        operations = vars(nested_value)
                        for op_name, op_value in operations.items():
                            if op_value is not strawberry.UNSET and op_name in FILTER_LOOKUPS:
                                q &= FILTER_LOOKUPS[op_name](field_path, op_value)
                    else:
                        q &= FILTER_LOOKUPS['exact'](field_path, nested_value)

                    used_fields.add(nested_field)
            continue

        # Handle direct filters and filter operations
        relationship_map, _ = get_relationship_map(model)
        transformed_field = relationship_map.get(field_name, field_name)
        if prefix:
            transformed_field = f'{prefix}__{transformed_field}'

        current_q = Q()
        if hasattr(value, '__dict__'):
            operations = vars(value)
            for op_name, op_value in operations.items():
                if op_value is not strawberry.UNSET and op_name in FILTER_LOOKUPS:
                    current_q &= FILTER_LOOKUPS[op_name](transformed_field, op_value)
        else:
            current_q = FILTER_LOOKUPS['exact'](transformed_field, value)

        q &= current_q

    return q, used_fields


# def build_filter_q(filters, prefix: str = '') -> tuple[Q, set[str]]:
#     q = Q()
#     used_fields = set()

#     for field_name, value in vars(filters).items():
#         if value is strawberry.UNSET or value is None:
#             continue

#         # Skip special fields
#         if field_name.startswith('__'):
#             continue

#         used_fields.add(field_name)
#         full_field = f"{prefix}{field_name}" if prefix else field_name

#         # Handle logical operators (AND, OR, NOT)
#         if field_name in ('AND', 'OR', 'NOT'):
#             items_q = []
#             filter_items = value if isinstance(value, (list, tuple)) else [value]

#             # First collect all the Q objects
#             for filter_item in filter_items:
#                 item_q, item_fields = build_filter_q(filter_item, prefix)
#                 used_fields.update(item_fields)
#                 items_q.append(item_q)

#             # Important change: Different handling based on operator
#             if field_name == 'AND':
#                 q &= reduce(operator.and_, items_q, Q())
#             elif field_name == 'OR':
#                 q |= reduce(operator.or_, items_q, Q())
#             else:  # NOT
#                 q &= ~reduce(operator.and_, items_q, Q())
#             continue

#         # Handle filter operation objects (like {i_exact: "value"})
#         current_q = Q()  # Create a separate Q object for this field
#         if hasattr(value, '__dict__'):
#             operations = vars(value)
#             for op_name, op_value in operations.items():
#                 if op_value is not strawberry.UNSET and op_name in FILTER_LOOKUPS:
#                     current_q &= FILTER_LOOKUPS[op_name](full_field, op_value)
#         else:
#             # Default exact match for direct values
#             current_q = FILTER_LOOKUPS['exact'](full_field, value)

#         # Add the field's conditions to the main Q object
#         q &= current_q

#     return q, used_fields


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
