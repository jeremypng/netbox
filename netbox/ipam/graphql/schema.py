from typing import List

import strawberry
import strawberry_django
from strawberry.types import Info

from .types import *
from .filters import *
from netbox.graphql.resolvers import list_resolver


@strawberry.type(name='Query')
class IPAMQuery:
    asn: ASNType = strawberry_django.field()

    @strawberry_django.field
    def asn_list(self, info: Info, filters: ASNFilter | None = strawberry.UNSET) -> List[ASNType]:
        queryset = ASNType.__strawberry_django_definition__.model.objects.all()
        queryset = ASNType.get_queryset(queryset, info)
        return list_resolver(info, queryset, filters)

    asn_range: ASNRangeType = strawberry_django.field()

    @strawberry_django.field
    def asn_range_list(self, info: Info, filters: ASNRangeFilter | None = strawberry.UNSET) -> List[ASNRangeType]:
        queryset = ASNRangeType.__strawberry_django_definition__.model.objects.all()
        queryset = ASNRangeType.get_queryset(queryset, info)
        return list_resolver(info, queryset, filters)

    aggregate: AggregateType = strawberry_django.field()

    @strawberry_django.field
    def aggregate_list(self, info: Info, filters: AggregateFilter | None = strawberry.UNSET) -> List[AggregateType]:
        queryset = AggregateType.__strawberry_django_definition__.model.objects.all()
        queryset = AggregateType.get_queryset(queryset, info)
        return list_resolver(info, queryset, filters)

    ip_address: IPAddressType = strawberry_django.field()

    @strawberry_django.field
    def ip_address_list(self, info: Info, filters: IPAddressFilter | None = strawberry.UNSET) -> List[IPAddressType]:
        queryset = IPAddressType.__strawberry_django_definition__.model.objects.all()
        queryset = IPAddressType.get_queryset(queryset, info)
        return list_resolver(info, queryset, filters)

    ip_range: IPRangeType = strawberry_django.field()

    @strawberry_django.field
    def ip_range_list(self, info: Info, filters: IPRangeFilter | None = strawberry.UNSET) -> List[IPRangeType]:
        queryset = IPRangeType.__strawberry_django_definition__.model.objects.all()
        queryset = IPRangeType.get_queryset(queryset, info)
        return list_resolver(info, queryset, filters)

    prefix: PrefixType = strawberry_django.field()

    @strawberry_django.field
    def prefix_list(self, info: Info, filters: PrefixFilter | None = strawberry.UNSET) -> List[PrefixType]:
        queryset = PrefixType.__strawberry_django_definition__.model.objects.all()
        queryset = PrefixType.get_queryset(queryset, info)
        return list_resolver(info, queryset, filters)

    rir: RIRType = strawberry_django.field()

    @strawberry_django.field
    def rir_list(self, info: Info, filters: RIRFilter | None = strawberry.UNSET) -> List[RIRType]:
        queryset = RIRType.__strawberry_django_definition__.model.objects.all()
        queryset = RIRType.get_queryset(queryset, info)
        return list_resolver(info, queryset, filters)

    role: RoleType = strawberry_django.field()

    @strawberry_django.field
    def role_list(self, info: Info, filters: RoleFilter | None = strawberry.UNSET) -> List[RoleType]:
        queryset = RoleType.__strawberry_django_definition__.model.objects.all()
        queryset = RoleType.get_queryset(queryset, info)
        return list_resolver(info, queryset, filters)

    route_target: RouteTargetType = strawberry_django.field()

    @strawberry_django.field
    def route_target_list(
        self, info: Info, filters: RouteTargetFilter | None = strawberry.UNSET
    ) -> List[RouteTargetType]:
        queryset = RouteTargetType.__strawberry_django_definition__.model.objects.all()
        queryset = RouteTargetType.get_queryset(queryset, info)
        return list_resolver(info, queryset, filters)

    service: ServiceType = strawberry_django.field()

    @strawberry_django.field
    def service_list(self, info: Info, filters: ServiceFilter | None = strawberry.UNSET) -> List[ServiceType]:
        queryset = ServiceType.__strawberry_django_definition__.model.objects.all()
        queryset = ServiceType.get_queryset(queryset, info)
        return list_resolver(info, queryset, filters)

    service_template: ServiceTemplateType = strawberry_django.field()

    @strawberry_django.field
    def service_template_list(
        self, info: Info, filters: ServiceTemplateFilter | None = strawberry.UNSET
    ) -> List[ServiceTemplateType]:
        queryset = ServiceTemplateType.__strawberry_django_definition__.model.objects.all()
        queryset = ServiceTemplateType.get_queryset(queryset, info)
        return list_resolver(info, queryset, filters)

    fhrp_group: FHRPGroupType = strawberry_django.field()

    @strawberry_django.field
    def fhrp_group_list(self, info: Info, filters: FHRPGroupFilter | None = strawberry.UNSET) -> List[FHRPGroupType]:
        queryset = FHRPGroupType.__strawberry_django_definition__.model.objects.all()
        queryset = FHRPGroupType.get_queryset(queryset, info)
        return list_resolver(info, queryset, filters)

    fhrp_group_assignment: FHRPGroupAssignmentType = strawberry_django.field()

    @strawberry_django.field
    def fhrp_group_assignment_list(
        self, info: Info, filters: FHRPGroupAssignmentFilter | None = strawberry.UNSET
    ) -> List[FHRPGroupAssignmentType]:
        queryset = FHRPGroupAssignmentType.__strawberry_django_definition__.model.objects.all()
        queryset = FHRPGroupAssignmentType.get_queryset(queryset, info)
        return list_resolver(info, queryset, filters)

    vlan: VLANType = strawberry_django.field()

    @strawberry_django.field
    def vlan_list(self, info: Info, filters: VLANFilter | None = strawberry.UNSET) -> List[VLANType]:
        queryset = VLANType.__strawberry_django_definition__.model.objects.all()
        queryset = VLANType.get_queryset(queryset, info)
        return list_resolver(info, queryset, filters)

    vlan_group: VLANGroupType = strawberry_django.field()

    @strawberry_django.field
    def vlan_group_list(self, info: Info, filters: VLANGroupFilter | None = strawberry.UNSET) -> List[VLANGroupType]:
        queryset = VLANGroupType.__strawberry_django_definition__.model.objects.all()
        queryset = VLANGroupType.get_queryset(queryset, info)
        return list_resolver(info, queryset, filters)

    vlan_translation_policy: VLANTranslationPolicyType = strawberry_django.field()

    @strawberry_django.field
    def vlan_translation_policy_list(
        self, info: Info, filters: VLANTranslationPolicyFilter | None = strawberry.UNSET
    ) -> List[VLANTranslationPolicyType]:
        queryset = VLANTranslationPolicyType.__strawberry_django_definition__.model.objects.all()
        queryset = VLANTranslationPolicyType.get_queryset(queryset, info)
        return list_resolver(info, queryset, filters)

    vlan_translation_rule: VLANTranslationRuleType = strawberry_django.field()

    @strawberry_django.field
    def vlan_translation_rule_list(
        self, info: Info, filters: VLANTranslationRuleFilter | None = strawberry.UNSET
    ) -> List[VLANTranslationRuleType]:
        queryset = VLANTranslationRuleType.__strawberry_django_definition__.model.objects.all()
        queryset = VLANTranslationRuleType.get_queryset(queryset, info)
        return list_resolver(info, queryset, filters)

    vrf: VRFType = strawberry_django.field()

    @strawberry_django.field
    def vrf_list(self, info: Info, filters: VRFFilter | None = strawberry.UNSET) -> List[VRFType]:
        queryset = VRFType.__strawberry_django_definition__.model.objects.all()
        queryset = VRFType.get_queryset(queryset, info)
        return list_resolver(info, queryset, filters)
