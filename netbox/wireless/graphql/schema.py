from typing import List

import strawberry
import strawberry_django
from strawberry.types import Info

from .types import *
from .filters import *
from netbox.graphql.resolvers import list_resolver


@strawberry.type(name='Query')
class WirelessQuery:
    wireless_lan: WirelessLANType = strawberry_django.field()

    @strawberry.field
    def wireless_lan_list(
        self, info: Info, filters: WirelessLANFilter | None = strawberry.UNSET
    ) -> List[WirelessLANType]:
        queryset = WirelessLANType.__strawberry_django_definition__.model.objects.all()
        queryset = WirelessLANType.get_queryset(queryset, info)
        return list_resolver(info, queryset, filters)

    wireless_lan_group: WirelessLANGroupType = strawberry_django.field()

    @strawberry.field
    def wireless_lan_group_list(
        self, info: Info, filters: WirelessLANGroupFilter | None = strawberry.UNSET
    ) -> List[WirelessLANGroupType]:
        queryset = WirelessLANGroupType.__strawberry_django_definition__.model.objects.all()
        queryset = WirelessLANGroupType.get_queryset(queryset, info)
        return list_resolver(info, queryset, filters)

    wireless_link: WirelessLinkType = strawberry_django.field()

    @strawberry.field
    def wireless_link_list(
        self, info: Info, filters: WirelessLinkFilter | None = strawberry.UNSET
    ) -> List[WirelessLinkType]:
        queryset = WirelessLinkType.__strawberry_django_definition__.model.objects.all()
        queryset = WirelessLinkType.get_queryset(queryset, info)
        return list_resolver(info, queryset, filters)
