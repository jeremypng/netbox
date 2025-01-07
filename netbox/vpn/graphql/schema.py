from typing import List

import strawberry
import strawberry_django
from strawberry.types import Info

from .types import *
from .filters import *
from netbox.graphql.resolvers import list_resolver


@strawberry.type(name='Query')
class VPNQuery:
    ike_policy: IKEPolicyType = strawberry_django.field()

    @strawberry.field
    def ike_policy_list(self, info: Info, filters: IKEPolicyFilter | None = strawberry.UNSET) -> List[IKEPolicyType]:
        queryset = IKEPolicyType.__strawberry_django_definition__.model.objects.all()
        queryset = IKEPolicyType.get_queryset(queryset, info)
        return list_resolver(info, queryset, filters)

    ike_proposal: IKEProposalType = strawberry_django.field()

    @strawberry.field
    def ike_proposal_list(
        self, info: Info, filters: IKEProposalFilter | None = strawberry.UNSET
    ) -> List[IKEProposalType]:
        queryset = IKEProposalType.__strawberry_django_definition__.model.objects.all()
        queryset = IKEProposalType.get_queryset(queryset, info)
        return list_resolver(info, queryset, filters)

    ipsec_policy: IPSecPolicyType = strawberry_django.field()

    @strawberry.field
    def ipsec_policy_list(
        self, info: Info, filters: IPSecPolicyFilter | None = strawberry.UNSET
    ) -> List[IPSecPolicyType]:
        queryset = IPSecPolicyType.__strawberry_django_definition__.model.objects.all()
        queryset = IPSecPolicyType.get_queryset(queryset, info)
        return list_resolver(info, queryset, filters)

    ipsec_profile: IPSecProfileType = strawberry_django.field()

    @strawberry.field
    def ipsec_profile_list(
        self, info: Info, filters: IPSecProfileFilter | None = strawberry.UNSET
    ) -> List[IPSecProfileType]:
        queryset = IPSecProfileType.__strawberry_django_definition__.model.objects.all()
        queryset = IPSecProfileType.get_queryset(queryset, info)
        return list_resolver(info, queryset, filters)

    ipsec_proposal: IPSecProposalType = strawberry_django.field()

    @strawberry.field
    def ipsec_proposal_list(
        self, info: Info, filters: IPSecProposalFilter | None = strawberry.UNSET
    ) -> List[IPSecProposalType]:
        queryset = IPSecProposalType.__strawberry_django_definition__.model.objects.all()
        queryset = IPSecProposalType.get_queryset(queryset, info)
        return list_resolver(info, queryset, filters)

    l2vpn: L2VPNType = strawberry_django.field()

    @strawberry.field
    def l2vpn_list(self, info: Info, filters: L2VPNFilter | None = strawberry.UNSET) -> List[L2VPNType]:
        queryset = L2VPNType.__strawberry_django_definition__.model.objects.all()
        queryset = L2VPNType.get_queryset(queryset, info)
        return list_resolver(info, queryset, filters)

    l2vpn_termination: L2VPNTerminationType = strawberry_django.field()

    @strawberry.field
    def l2vpn_termination_list(
        self, info: Info, filters: L2VPNTerminationFilter | None = strawberry.UNSET
    ) -> List[L2VPNTerminationType]:
        queryset = L2VPNTerminationType.__strawberry_django_definition__.model.objects.all()
        queryset = L2VPNTerminationType.get_queryset(queryset, info)
        return list_resolver(info, queryset, filters)

    tunnel: TunnelType = strawberry_django.field()

    @strawberry.field
    def tunnel_list(self, info: Info, filters: TunnelFilter | None = strawberry.UNSET) -> List[TunnelType]:
        queryset = TunnelType.__strawberry_django_definition__.model.objects.all()
        queryset = TunnelType.get_queryset(queryset, info)
        return list_resolver(info, queryset, filters)

    tunnel_group: TunnelGroupType = strawberry_django.field()

    @strawberry.field
    def tunnel_group_list(
        self, info: Info, filters: TunnelGroupFilter | None = strawberry.UNSET
    ) -> List[TunnelGroupType]:
        queryset = TunnelGroupType.__strawberry_django_definition__.model.objects.all()
        queryset = TunnelGroupType.get_queryset(queryset, info)
        return list_resolver(info, queryset, filters)

    tunnel_termination: TunnelTerminationType = strawberry_django.field()

    @strawberry.field
    def tunnel_termination_list(
        self, info: Info, filters: TunnelTerminationFilter | None = strawberry.UNSET
    ) -> List[TunnelTerminationType]:
        queryset = TunnelTerminationType.__strawberry_django_definition__.model.objects.all()
        queryset = TunnelTerminationType.get_queryset(queryset, info)
        return list_resolver(info, queryset, filters)
