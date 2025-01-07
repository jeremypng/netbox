from typing import List

import strawberry
import strawberry_django
from strawberry.types import Info

from .types import *
from .filters import *
from netbox.graphql.resolvers import list_resolver


@strawberry.type(name='Query')
class VirtualizationQuery:
    cluster: ClusterType = strawberry_django.field()

    @strawberry_django.field
    def cluster_list(self, info: Info, filters: ClusterFilter | None = strawberry.UNSET) -> List[ClusterType]:
        queryset = ClusterType.__strawberry_django_definition__.model.objects.all()
        queryset = ClusterType.get_queryset(queryset, info)
        return list_resolver(info, queryset, filters)

    cluster_group: ClusterGroupType = strawberry_django.field()

    @strawberry_django.field
    def cluster_group_list(
        self, info: Info, filters: ClusterGroupFilter | None = strawberry.UNSET
    ) -> List[ClusterGroupType]:
        queryset = ClusterGroupType.__strawberry_django_definition__.model.objects.all()
        queryset = ClusterGroupType.get_queryset(queryset, info)
        return list_resolver(info, queryset, filters)

    cluster_type: ClusterTypeType = strawberry_django.field()

    @strawberry_django.field
    def cluster_type_list(
        self, info: Info, filters: ClusterTypeFilter | None = strawberry.UNSET
    ) -> List[ClusterTypeType]:
        queryset = ClusterTypeType.__strawberry_django_definition__.model.objects.all()
        queryset = ClusterTypeType.get_queryset(queryset, info)
        return list_resolver(info, queryset, filters)

    virtual_machine: VirtualMachineType = strawberry_django.field()

    @strawberry_django.field
    def virtual_machine_list(
        self, info: Info, filters: VirtualMachineFilter | None = strawberry.UNSET
    ) -> List[VirtualMachineType]:
        queryset = VirtualMachineType.__strawberry_django_definition__.model.objects.all()
        queryset = VirtualMachineType.get_queryset(queryset, info)
        return list_resolver(info, queryset, filters)

    vm_interface: VMInterfaceType = strawberry_django.field()

    @strawberry_django.field
    def vm_interface_list(
        self, info: Info, filters: VMInterfaceFilter | None = strawberry.UNSET
    ) -> List[VMInterfaceType]:
        queryset = VMInterfaceType.__strawberry_django_definition__.model.objects.all()
        queryset = VMInterfaceType.get_queryset(queryset, info)
        return list_resolver(info, queryset, filters)

    virtual_disk: VirtualDiskType = strawberry_django.field()

    @strawberry_django.field
    def virtual_disk_list(
        self, info: Info, filters: VirtualDiskFilter | None = strawberry.UNSET
    ) -> List[VirtualDiskType]:
        queryset = VirtualDiskType.__strawberry_django_definition__.model.objects.all()
        queryset = VirtualDiskType.get_queryset(queryset, info)
        return list_resolver(info, queryset, filters)
