import strawberry
from django.conf import settings
from strawberry_django.optimizer import DjangoOptimizerExtension
from strawberry.extensions import MaxAliasesLimiter
from strawberry.schema.config import StrawberryConfig

from circuits.graphql.schema import CircuitsQuery
from core.graphql.schema import CoreQuery
from dcim.graphql.schema import DCIMQuery
from extras.graphql.schema import ExtrasQuery
from ipam.graphql.schema import IPAMQuery
from netbox.registry import registry
from tenancy.graphql.schema import TenancyQuery
from users.graphql.schema import UsersQuery
from virtualization.graphql.schema import VirtualizationQuery
from vpn.graphql.schema import VPNQuery
from wireless.graphql.schema import WirelessQuery

from .filter_mixins import FilterSchemaBuilder


def unwrap_type(field_type):
    """Recursively unwrap a Strawberry type until we get to the base type"""
    if hasattr(field_type, 'of_type'):  # List or Optional wrapper
        return unwrap_type(field_type.of_type)
    return field_type


def finalize_filters():
    # Second pass: Create complete filters
    rebuilt_filters = FilterSchemaBuilder.rebuild_filters()

    query_classes = [UsersQuery, CircuitsQuery, CoreQuery, DCIMQuery, ExtrasQuery,
                    IPAMQuery, TenancyQuery, VirtualizationQuery, VPNQuery, WirelessQuery]

    for query_class in query_classes:
        if hasattr(query_class, '__strawberry_definition__'):
            type_definition = query_class.__strawberry_definition__

            for field in type_definition.fields:
                for arg in field.arguments:
                    if arg.python_name == 'filters':
                        filter_type = unwrap_type(arg.type)
                        if hasattr(filter_type, 'filterset'):
                            model_path = filter_type.filterset._meta.model.__module__
                            model_path = model_path + "." + filter_type.filterset._meta.model.__name__
                            if model_path in rebuilt_filters:
                                rebuilt_filter = rebuilt_filters[model_path]
                                # Only copy specific attributes, avoiding deprecated ones
                                attrs_to_copy = [
                                    '__annotations__',
                                    '__strawberry_definition__',
                                    '__strawberry_django_definition__',
                                    'filterset'
                                ]
                                for attr in attrs_to_copy:
                                    if hasattr(rebuilt_filter, attr):
                                        setattr(filter_type, attr, getattr(rebuilt_filter, attr))
    return True


finalized_filter_status = finalize_filters()
if not finalized_filter_status:
    raise Exception("Failed to finalize filters")


@strawberry.type
class Query(
    UsersQuery,
    CircuitsQuery,
    CoreQuery,
    DCIMQuery,
    ExtrasQuery,
    IPAMQuery,
    TenancyQuery,
    VirtualizationQuery,
    VPNQuery,
    WirelessQuery,
    *registry['plugins']['graphql_schemas'],  # Append plugin schemas
):
    pass


schema = strawberry.Schema(
    query=Query,
    config=StrawberryConfig(auto_camel_case=False),
    extensions=[
        DjangoOptimizerExtension(prefetch_custom_queryset=True),
        MaxAliasesLimiter(max_alias_count=settings.GRAPHQL_MAX_ALIASES),
    ]
)
