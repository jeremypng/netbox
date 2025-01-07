from typing import List

import strawberry
import strawberry_django
from strawberry.types import Info

from .types import *
from .filters import *
from netbox.graphql.resolvers import list_resolver


@strawberry.type(name='Query')
class CircuitsQuery:
    circuit: CircuitType = strawberry_django.field()

    @strawberry_django.field
    def circuit_list(self, info: Info, filters: CircuitFilter | None = strawberry.UNSET) -> List[CircuitType]:
        queryset = CircuitType.__strawberry_django_definition__.model.objects.all()
        queryset = CircuitType.get_queryset(queryset, info)
        return list_resolver(info, queryset, filters)

    circuit_termination: CircuitTerminationType = strawberry_django.field()

    @strawberry_django.field
    def circuit_termination_list(
        self, info: Info, filters: CircuitTerminationFilter | None = strawberry.UNSET
    ) -> List[CircuitTerminationType]:
        queryset = CircuitTerminationType.__strawberry_django_definition__.model.objects.all()
        queryset = CircuitTerminationType.get_queryset(queryset, info)
        return list_resolver(info, queryset, filters)

    circuit_type: CircuitTypeType = strawberry_django.field()

    @strawberry_django.field
    def circuit_type_list(
        self, info: Info, filters: CircuitTypeFilter | None = strawberry.UNSET
    ) -> List[CircuitTypeType]:
        queryset = CircuitTypeType.__strawberry_django_definition__.model.objects.all()
        queryset = CircuitTypeType.get_queryset(queryset, info)
        return list_resolver(info, queryset, filters)

    circuit_group: CircuitGroupType = strawberry_django.field()

    @strawberry_django.field
    def circuit_group_list(
        self, info: Info, filters: CircuitGroupFilter | None = strawberry.UNSET
    ) -> List[CircuitGroupType]:
        queryset = CircuitGroupType.__strawberry_django_definition__.model.objects.all()
        queryset = CircuitGroupType.get_queryset(queryset, info)
        return list_resolver(info, queryset, filters)

    circuit_group_assignment: CircuitGroupAssignmentType = strawberry_django.field()

    @strawberry_django.field
    def circuit_group_assignment_list(
        self, info: Info, filters: CircuitGroupAssignmentFilter | None = strawberry.UNSET
    ) -> List[CircuitGroupAssignmentType]:
        queryset = CircuitGroupAssignmentType.__strawberry_django_definition__.model.objects.all()
        queryset = CircuitGroupAssignmentType.get_queryset(queryset, info)
        return list_resolver(info, queryset, filters)

    provider: ProviderType = strawberry_django.field()

    @strawberry_django.field
    def provider_list(self, info: Info, filters: ProviderFilter | None = strawberry.UNSET) -> List[ProviderType]:
        queryset = ProviderType.__strawberry_django_definition__.model.objects.all()
        queryset = ProviderType.get_queryset(queryset, info)
        return list_resolver(info, queryset, filters)

    provider_account: ProviderAccountType = strawberry_django.field()

    @strawberry_django.field
    def provider_account_list(
        self, info: Info, filters: ProviderAccountFilter | None = strawberry.UNSET
    ) -> List[ProviderAccountType]:
        queryset = ProviderAccountType.__strawberry_django_definition__.model.objects.all()
        queryset = ProviderAccountType.get_queryset(queryset, info)
        return list_resolver(info, queryset, filters)

    provider_network: ProviderNetworkType = strawberry_django.field()

    @strawberry_django.field
    def provider_network_list(
        self, info: Info, filters: ProviderNetworkFilter | None = strawberry.UNSET
    ) -> List[ProviderNetworkType]:
        queryset = ProviderNetworkType.__strawberry_django_definition__.model.objects.all()
        queryset = ProviderNetworkType.get_queryset(queryset, info)
        return list_resolver(info, queryset, filters)

    virtual_circuit: VirtualCircuitType = strawberry_django.field()

    @strawberry_django.field
    def virtual_circuit_list(
        self, info: Info, filters: VirtualCircuitFilter | None = strawberry.UNSET
    ) -> List[VirtualCircuitType]:
        queryset = VirtualCircuitType.__strawberry_django_definition__.model.objects.all()
        queryset = VirtualCircuitType.get_queryset(queryset, info)
        return list_resolver(info, queryset, filters)

    virtual_circuit_termination: VirtualCircuitTerminationType = strawberry_django.field()

    @strawberry_django.field
    def virtual_circuit_termination_list(
        self, info: Info, filters: VirtualCircuitTerminationFilter | None = strawberry.UNSET
    ) -> List[VirtualCircuitTerminationType]:
        queryset = VirtualCircuitTerminationType.__strawberry_django_definition__.model.objects.all()
        queryset = VirtualCircuitTerminationType.get_queryset(queryset, info)
        return list_resolver(info, queryset, filters)

    virtual_circuit_type: VirtualCircuitTypeType = strawberry_django.field()

    @strawberry_django.field
    def virtual_circuit_type_list(
        self, info: Info, filters: VirtualCircuitTypeFilter | None = strawberry.UNSET
    ) -> List[VirtualCircuitTypeType]:
        queryset = VirtualCircuitTypeType.__strawberry_django_definition__.model.objects.all()
        queryset = VirtualCircuitTypeType.get_queryset(queryset, info)
        return list_resolver(info, queryset, filters)
