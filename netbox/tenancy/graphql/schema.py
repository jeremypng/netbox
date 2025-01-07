from typing import List

import strawberry
import strawberry_django
from strawberry.types import Info

from .types import *
from .filters import *
from netbox.graphql.resolvers import list_resolver


@strawberry.type(name='Query')
class TenancyQuery:
    tenant: TenantType = strawberry_django.field()

    @strawberry_django.field
    def tenant_list(self, info: Info, filters: TenantFilter | None = strawberry.UNSET) -> List[TenantType]:
        queryset = TenantType.__strawberry_django_definition__.model.objects.all()
        queryset = TenantType.get_queryset(queryset, info)
        return list_resolver(info, queryset, filters)

    tenant_group: TenantGroupType = strawberry_django.field()

    @strawberry_django.field
    def tenant_group_list(
        self, info: Info, filters: TenantGroupFilter | None = strawberry.UNSET
    ) -> List[TenantGroupType]:
        queryset = TenantGroupType.__strawberry_django_definition__.model.objects.all()
        queryset = TenantGroupType.get_queryset(queryset, info)
        return list_resolver(info, queryset, filters)

    contact: ContactType = strawberry_django.field()

    @strawberry_django.field
    def contact_list(self, info: Info, filters: ContactFilter | None = strawberry.UNSET) -> List[ContactType]:
        queryset = ContactType.__strawberry_django_definition__.model.objects.all()
        queryset = ContactType.get_queryset(queryset, info)
        return list_resolver(info, queryset, filters)

    contact_role: ContactRoleType = strawberry_django.field()

    @strawberry_django.field
    def contact_role_list(
        self, info: Info, filters: ContactRoleFilter | None = strawberry.UNSET
    ) -> List[ContactRoleType]:
        queryset = ContactRoleType.__strawberry_django_definition__.model.objects.all()
        queryset = ContactRoleType.get_queryset(queryset, info)
        return list_resolver(info, queryset, filters)

    contact_group: ContactGroupType = strawberry_django.field()

    @strawberry_django.field
    def contact_group_list(
        self, info: Info, filters: ContactGroupFilter | None = strawberry.UNSET
    ) -> List[ContactGroupType]:
        queryset = ContactGroupType.__strawberry_django_definition__.model.objects.all()
        queryset = ContactGroupType.get_queryset(queryset, info)
        return list_resolver(info, queryset, filters)

    contact_assignment: ContactAssignmentType = strawberry_django.field()

    @strawberry_django.field
    def contact_assignment_list(
        self, info: Info, filters: ContactAssignmentFilter | None = strawberry.UNSET
    ) -> List[ContactAssignmentType]:
        queryset = ContactAssignmentType.__strawberry_django_definition__.model.objects.all()
        queryset = ContactAssignmentType.get_queryset(queryset, info)
        return list_resolver(info, queryset, filters)
