from typing import List

import strawberry
import strawberry_django
from strawberry.types import Info

from .types import *
from .filters import *
from netbox.graphql.resolvers import list_resolver


@strawberry.type(name='Query')
class CoreQuery:
    data_file: DataFileType = strawberry_django.field()

    @strawberry_django.field
    def data_file_list(self, info: Info, filters: DataFileFilter | None = strawberry.UNSET) -> List[DataFileType]:
        queryset = DataFileType.__strawberry_django_definition__.model.objects.all()
        queryset = DataFileType.get_queryset(queryset, info)
        return list_resolver(info, queryset, filters)

    data_source: DataSourceType = strawberry_django.field()

    @strawberry_django.field
    def data_source_list(self, info: Info, filters: DataSourceFilter | None = strawberry.UNSET) -> List[DataSourceType]:
        queryset = DataSourceType.__strawberry_django_definition__.model.objects.all()
        queryset = DataSourceType.get_queryset(queryset, info)
        return list_resolver(info, queryset, filters)
