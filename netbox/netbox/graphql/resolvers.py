from typing import Optional
import strawberry
import strawberry_django
from strawberry.types import Info

from utilities.querysets import RestrictedQuerySet

from .filter_mixins import BaseFilterMixin


def list_resolver(
    info: Info,
    queryset: RestrictedQuerySet,
    filters: Optional[BaseFilterMixin] = strawberry.UNSET,
):
    """
    Resolver used for list queries to help filter custom fields.
    After this is returned, the normal strawberry_django filter is processed without the custom field filter.
    """
    if filters and filters is not strawberry.UNSET and len(getattr(filters, '__netbox_field_map__', [])):
        queryset, q_filter = strawberry_django.filters.process_filters(filters, queryset, info)

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

        return queryset.filter(q_filter)

    return queryset
