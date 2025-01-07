from typing import List

import strawberry
import strawberry_django
from strawberry.types import Info

from .types import *
from .filters import *
from netbox.graphql.resolvers import list_resolver


@strawberry.type(name='Query')
class UsersQuery:
    group: GroupType = strawberry_django.field()

    @strawberry.field
    def group_list(self, info: Info, filters: GroupFilter | None = strawberry.UNSET) -> List[GroupType]:
        queryset = GroupType.__strawberry_django_definition__.model.objects.all()
        queryset = GroupType.get_queryset(queryset, info)
        return list_resolver(info, queryset, filters)

    user: UserType = strawberry_django.field()

    @strawberry.field
    def user_list(self, info: Info, filters: UserFilter | None = strawberry.UNSET) -> List[UserType]:
        queryset = UserType.__strawberry_django_definition__.model.objects.all()
        queryset = UserType.get_queryset(queryset, info)
        return list_resolver(info, queryset, filters)
