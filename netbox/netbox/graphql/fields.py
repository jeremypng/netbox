from strawberry_django import optimizer
from strawberry_django.fields.field import StrawberryDjangoField
from strawberry_django.fields.base import StrawberryDjangoFieldBase
from strawberry_django.optimizer import is_optimized_by_prefetching
from strawberry_django.permissions import filter_with_perms
from strawberry_django.queryset import run_type_get_queryset

from .utils import build_filter_q  # Assuming you put the filter utils in utils.py


class CustomStrawberryDjangoField(StrawberryDjangoField):
    def get_queryset(self, queryset, info, **kwargs):
        # If the queryset been optimized at prefetch phase, this function has already been
        # called by the optimizer extension, meaning we don't want to call it again
        if is_optimized_by_prefetching(queryset):
            return queryset

        queryset = run_type_get_queryset(queryset, self.django_type, info)

        # Get filters from kwargs
        filters = kwargs.get('filters')
        if filters:
            # Build our filter
            q_filter = build_filter_q(filters)
            if q_filter:
                queryset = queryset.filter(q_filter)

        # Handle permission filtering but skip the parent's filter handling
        queryset = StrawberryDjangoFieldBase.get_queryset(
            self,
            filter_with_perms(queryset, info),
            info,
            **kwargs
        )

        # Handle optimization
        ext = optimizer.optimizer.get()
        if ext is not None:
            queryset = ext.optimize(queryset, info=info)

        return queryset
