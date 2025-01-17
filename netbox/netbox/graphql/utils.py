from django.db.models import Q
import strawberry
from typing import Any


def build_filter_q(filters: Any) -> Q:
    """Build Django Q objects from filter values"""
    q = Q()

    for field_name, value in vars(filters).items():
        # Skip special fields and unset values
        if field_name.startswith('__') or value is strawberry.UNSET:
            continue

        # Handle exact matches
        if value is not None:
            q &= Q(**{field_name: value})

    return q
