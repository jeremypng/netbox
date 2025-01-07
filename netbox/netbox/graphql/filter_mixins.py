from typing import TypeVar

from datetime import datetime, date, time
from django.db.utils import ProgrammingError, OperationalError
from django.db.models.fields import BigAutoField, BigIntegerField, BooleanField, CharField, DateField, DateTimeField
from django.db.models.fields import EmailField, GenericIPAddressField, IntegerField, PositiveIntegerField, SlugField
from django.db.models.fields import TextField, URLField
import django_filters
import strawberry
from strawberry_django import FilterLookup, ComparisonFilterLookup, DateFilterLookup, DatetimeFilterLookup
from strawberry_django import TimeFilterLookup
from django.core.exceptions import FieldDoesNotExist

from netbox.graphql.scalars import BigInt
from utilities.filters import *

T = TypeVar('T')


def map_strawberry_type(field):
    attr_type = None

    # Django Field types
    if isinstance(field, BigAutoField):
        attr_type = ComparisonFilterLookup[BigInt] | None
    elif isinstance(field, BigIntegerField):
        attr_type = ComparisonFilterLookup[BigInt] | None
    elif isinstance(field, BooleanField):
        attr_type = bool | None
    elif isinstance(field, CharField):
        attr_type = FilterLookup[str] | None
    elif isinstance(field, DateField):
        attr_type = DateFilterLookup[date] | None
    elif isinstance(field, DateTimeField):
        attr_type = DatetimeFilterLookup[datetime] | None
    elif isinstance(field, EmailField):
        attr_type = FilterLookup[str] | None
    elif isinstance(field, GenericIPAddressField):
        attr_type = FilterLookup[str] | None
    elif isinstance(field, IntegerField):
        attr_type = ComparisonFilterLookup[int] | None
    elif isinstance(field, PositiveIntegerField):
        attr_type = ComparisonFilterLookup[int] | None
    elif isinstance(field, SlugField):
        attr_type = FilterLookup[str] | None
    elif isinstance(field, TextField):
        attr_type = FilterLookup[str] | None
    elif isinstance(field, URLField):
        attr_type = FilterLookup[str] | None

    # NetBox Filter types - put base classes after derived classes
    if isinstance(field, ContentTypeFilter):
        attr_type = FilterLookup[str] | None
    elif isinstance(field, MultiValueArrayFilter):
        pass
    elif isinstance(field, MultiValueCharFilter):
        attr_type = FilterLookup[str] | None
    elif isinstance(field, MultiValueDateFilter):
        attr_type = DateFilterLookup[date] | None
    elif isinstance(field, MultiValueDateTimeFilter):
        attr_type = DatetimeFilterLookup[datetime] | None
    elif isinstance(field, MultiValueDecimalFilter):
        attr_type = ComparisonFilterLookup[float] | None
    elif isinstance(field, MultiValueMACAddressFilter):
        attr_type = FilterLookup[str] | None
    elif isinstance(field, MultiValueNumberFilter):
        attr_type = ComparisonFilterLookup[int] | None
    elif isinstance(field, MultiValueTimeFilter):
        attr_type = TimeFilterLookup[time] | None
    elif isinstance(field, MultiValueWWNFilter):
        attr_type = FilterLookup[str] | None
    elif isinstance(field, NullableCharFieldFilter):
        attr_type = FilterLookup[str] | None
    elif isinstance(field, NumericArrayFilter):
        attr_type = ComparisonFilterLookup[int] | None
    elif isinstance(field, TreeNodeMultipleChoiceFilter):
        attr_type = FilterLookup[str] | None

    # From django_filters - ordering of these matters as base classes must
    # come after derived classes so the base class doesn't get matched first
    # a pass for the check (no attr_type) means we don't currently handle
    # or use that type
    elif issubclass(type(field), django_filters.OrderingFilter):
        pass
    elif issubclass(type(field), django_filters.BaseRangeFilter):
        pass
    elif issubclass(type(field), django_filters.BaseInFilter):
        pass
    elif issubclass(type(field), django_filters.LookupChoiceFilter):
        pass
    elif issubclass(type(field), django_filters.AllValuesMultipleFilter):
        pass
    elif issubclass(type(field), django_filters.AllValuesFilter):
        pass
    elif issubclass(type(field), django_filters.TimeRangeFilter):
        pass
    elif issubclass(type(field), django_filters.IsoDateTimeFromToRangeFilter):
        attr_type = DatetimeFilterLookup[datetime] | None
    elif issubclass(type(field), django_filters.DateTimeFromToRangeFilter):
        attr_type = DatetimeFilterLookup[datetime] | None
    elif issubclass(type(field), django_filters.DateFromToRangeFilter):
        attr_type = DateFilterLookup[date] | None
    elif issubclass(type(field), django_filters.DateRangeFilter):
        attr_type = DateFilterLookup[date] | None
    elif issubclass(type(field), django_filters.RangeFilter):
        attr_type = ComparisonFilterLookup[int] | None
    elif issubclass(type(field), django_filters.NumericRangeFilter):
        attr_type = ComparisonFilterLookup[int] | None
    elif issubclass(type(field), django_filters.NumberFilter):
        attr_type = ComparisonFilterLookup[int] | None
    elif issubclass(type(field), django_filters.ModelMultipleChoiceFilter):
        if (fieldname := getattr(field, "field_name")) and fieldname.endswith('_id'):
            attr_type = int | None
        else:
            attr_type = str | None
    elif issubclass(type(field), django_filters.ModelChoiceFilter):
        attr_type = str | None
    elif issubclass(type(field), django_filters.DurationFilter):
        attr_type = FilterLookup[str] | None
    elif issubclass(type(field), django_filters.IsoDateTimeFilter):
        attr_type = DatetimeFilterLookup[datetime] | None
    elif issubclass(type(field), django_filters.DateTimeFilter):
        attr_type = DatetimeFilterLookup[datetime] | None
    elif issubclass(type(field), django_filters.TimeFilter):
        attr_type = TimeFilterLookup[time] | None
    elif issubclass(type(field), django_filters.DateFilter):
        attr_type = DateFilterLookup[date] | None
    elif issubclass(type(field), django_filters.TypedMultipleChoiceFilter):
        attr_type = FilterLookup[str] | None
    elif issubclass(type(field), django_filters.MultipleChoiceFilter):
        attr_type = str | None
    elif issubclass(type(field), django_filters.TypedChoiceFilter):
        attr_type = FilterLookup[str] | None
    elif issubclass(type(field), django_filters.ChoiceFilter):
        attr_type = FilterLookup[str] | None
    elif issubclass(type(field), django_filters.BooleanFilter):
        attr_type = bool | None
    elif issubclass(type(field), django_filters.UUIDFilter):
        attr_type = FilterLookup[str] | None
    elif issubclass(type(field), django_filters.CharFilter):
        # looks like only used by 'q'
        attr_type = FilterLookup[str] | None

    return attr_type


def autotype_decorator(filterset):
    """
    Decorator used to auto creates a dataclass used by Strawberry based on a filterset.
    Must go after the Strawberry decorator as follows:

    @strawberry_django.filter(models.Example, lookups=True)
    @autotype_decorator(filtersets.ExampleFilterSet)
    class ExampleFilter(BaseFilterMixin):
        pass

    The Filter itself must be derived from BaseFilterMixin.  For items listed in meta.fields
    of the filterset, usually just a type specifier is generated, so for
    `fields = [created, ]` the dataclass would be:

    class ExampleFilter(BaseFilterMixin):
        created: auto

    For other filter fields a function needs to be created for Strawberry with the
    naming convention `filter_{fieldname}` which is auto detected and called by
    Strawberry, this function uses the filterset to handle the query.
    """

    def create_attribute(cls, fieldname, attr_type, custom_field=False):
        if fieldname not in cls.__annotations__ and attr_type:
            cls.__annotations__[fieldname] = attr_type

    def wrapper(cls):
        cls.filterset = filterset
        fields = filterset.get_fields()
        model = filterset._meta.model

        # Handle regular model fields
        for fieldname in fields.keys():
            attr_type = None
            if fieldname not in cls.__annotations__:
                try:
                    field = model._meta.get_field(fieldname)
                except FieldDoesNotExist:
                    continue

                attr_type = map_strawberry_type(field)

                create_attribute(cls, fieldname, attr_type)

        # Handle filterset declared filters
        declared_filters = filterset.declared_filters
        for fieldname, field in declared_filters.items():
            attr_type = map_strawberry_type(field)
            if attr_type is None:
                raise NotImplementedError(f'GraphQL Filter field unknown: {fieldname}: {field}')

            create_attribute(cls, fieldname, attr_type)

        # Handle runtime custom field filters with an instance of the filterset
        # This will fail if the database does not exist yet (ie: on first startup)
        # so we need to catch the exception and continue
        try:
            filterset_instance = filterset()
        except ProgrammingError:
            # Occurs when initial database migrations have not been applied.
            return cls
        except OperationalError:
            # Occurs during testing if there is no database as defined in configuration_testing.py
            return cls

        # Handle custom field filters and build a translation map for use in the resolver
        if filterset_instance:
            cls.__netbox_field_map__ = {}
            for filter_name, filter in filterset_instance.filters.items():
                if (
                    getattr(filter, 'custom_field', None)
                    and filter_name.find('__') == -1
                    and filter_name not in cls.__annotations__
                ):
                    custom_field = True
                    attr_type = map_strawberry_type(filter)
                    if attr_type is not None:
                        create_attribute(cls, filter_name, attr_type, custom_field)
                    if filter.field_name:
                        cls.__netbox_field_map__[filter_name] = filter.field_name

        return cls

    return wrapper


@strawberry.input
class BaseFilterMixin: ...
