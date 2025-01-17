import inspect
from typing import TypeVar

from datetime import datetime, date, time
from django.db.utils import ProgrammingError, OperationalError
from django.db.models.fields import BigAutoField, BigIntegerField, BooleanField, CharField, DateField, DateTimeField
from django.db.models.fields import EmailField, GenericIPAddressField, IntegerField, PositiveIntegerField, SlugField
from django.db.models.fields import TextField, URLField
from django.db.models.fields.related_descriptors import (ForwardManyToOneDescriptor,
    ReverseManyToOneDescriptor
)
import django_filters
import strawberry
from strawberry_django import FilterLookup, ComparisonFilterLookup, DateFilterLookup, DatetimeFilterLookup
from strawberry_django import TimeFilterLookup
from django.core.exceptions import FieldDoesNotExist

from netbox.graphql.scalars import BigInt
from utilities.filters import *

T = TypeVar('T')


class FilterSchemaBuilder:
    _filter_stubs = {}
    _relationships = {}

    @classmethod
    def register_filter(cls, model, original_filter):
        model_path = f"{model.__module__}.{model.__name__}"
        if model_path not in cls._filter_stubs:
            cls._filter_stubs[model_path] = original_filter

    @classmethod
    def register_relationship(cls, source_model, field_name, target_model):
        source_path = f"{source_model.__module__}.{source_model.__name__}"
        if source_path not in cls._relationships:
            cls._relationships[source_path] = []
        # Don't register self-referential relationships
        if source_model != target_model:
            cls._relationships[source_path].append((field_name, target_model))

    @classmethod
    def rebuild_filters(cls):
        from strawberry_django import filter as strawberry_filter

        rebuilt_filters = {}
        for model_path, original_filter in cls._filter_stubs.items():
            model = original_filter.filterset._meta.model

            # Get original annotations from autotype decorator
            original_annotations = getattr(original_filter, '__annotations__', {})
            annotations = original_annotations.copy()  # Make a copy to not modify original

            # Add relationships, excluding self-references
            relationships = cls._relationships.get(model_path, [])
            for field_name, target_model in relationships:
                target_path = f"{target_model.__module__}.{target_model.__name__}"
                target_filter = cls._filter_stubs.get(target_path)
                if target_filter and target_model != model:  # Exclude self-references
                    annotations[field_name] = target_filter | None

            # Create new filter with combined annotations
            new_filter = type(
                f"{model.__name__}Filter",
                (BaseFilterMixin,),
                {
                    "__annotations__": annotations,
                    "__relationships__": relationships  # Store relationship info
                }
            )

            decorated_filter = strawberry_filter(model, lookups=True)(new_filter)
            rebuilt_filters[model_path] = decorated_filter

        return rebuilt_filters


def map_strawberry_type(field):
    attr_type = None
    register_relationship = False

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
        register_relationship = True
    elif issubclass(type(field), django_filters.ModelChoiceFilter):
        register_relationship = True
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

    return attr_type, register_relationship


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

                attr_type, _ = map_strawberry_type(field)

                create_attribute(cls, fieldname, attr_type)

        # Handle related ManyToOne fields
        many_to_one_fields = [attr[0] for attr in inspect.getmembers(model) if isinstance(attr[1],
            ForwardManyToOneDescriptor)]
        for fieldname in many_to_one_fields:
            if fieldname not in cls.__annotations__:
                model_field = getattr(model, fieldname)
                related_model = model_field.field.related_model
                FilterSchemaBuilder.register_relationship(model, fieldname, related_model)

        # Handle related ReverseManyToOneDescriptor fields
        reverse_many_to_one_fields = [attr[0] for attr in inspect.getmembers(model) if isinstance(attr[1],
            ReverseManyToOneDescriptor)]
        for fieldname in reverse_many_to_one_fields:
            if fieldname not in cls.__annotations__:
                model_field = getattr(model, fieldname)
                related_model = model_field.rel.related_model
                FilterSchemaBuilder.register_relationship(model, fieldname, related_model)

        # Handle filterset declared filters
        declared_filters = filterset.declared_filters
        for fieldname, field in declared_filters.items():
            attr_type, register_relationship = map_strawberry_type(field)
            if (isinstance(field, django_filters.ModelMultipleChoiceFilter) or
                isinstance(field, django_filters.ModelChoiceFilter)) and fieldname.endswith('_id'):
                attr_type = int | None
            elif register_relationship:
                if getattr(field.queryset, 'model', None):
                    related_model = field.queryset.model
                    FilterSchemaBuilder.register_relationship(model, fieldname, related_model)
                    continue
            else:
                attr_type, _ = map_strawberry_type(field)
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
                    attr_type, _ = map_strawberry_type(filter)
                    if attr_type is not None:
                        create_attribute(cls, filter_name, attr_type, custom_field)
                    if filter.field_name:
                        cls.__netbox_field_map__[filter_name] = filter.field_name

        # Register original class and create stub
        FilterSchemaBuilder.register_filter(model, cls)

        return cls

    return wrapper


@strawberry.input
class BaseFilterMixin: ...
