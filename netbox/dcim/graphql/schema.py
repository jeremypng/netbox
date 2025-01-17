from typing import List

import strawberry
import strawberry_django
from strawberry.types import Info

from .types import *
from .filters import *
from netbox.graphql.resolvers import list_resolver

from netbox.graphql.fields import CustomStrawberryDjangoField


@strawberry.type(name='Query')
class DCIMQuery:
    cable: CableType = strawberry_django.field()

    @strawberry_django.field(field_cls=CustomStrawberryDjangoField)
    def cable_list(self, info: Info, filters: CableFilter | None = strawberry.UNSET) -> List[CableType]:
        queryset = CableType.__strawberry_django_definition__.model.objects.all()
        queryset = CableType.get_queryset(queryset, info)
        return list_resolver(info, queryset, filters)

    console_port: ConsolePortType = strawberry_django.field()

    @strawberry_django.field(field_cls=CustomStrawberryDjangoField)
    def console_port_list(
        self, info: Info, filters: ConsolePortFilter | None = strawberry.UNSET
    ) -> List[ConsolePortType]:
        queryset = ConsolePortType.__strawberry_django_definition__.model.objects.all()
        queryset = ConsolePortType.get_queryset(queryset, info)
        return list_resolver(info, queryset, filters)

    console_port_template: ConsolePortTemplateType = strawberry_django.field()

    @strawberry_django.field(field_cls=CustomStrawberryDjangoField)
    def console_port_template_list(
        self, info: Info, filters: ConsolePortTemplateFilter | None = strawberry.UNSET
    ) -> List[ConsolePortTemplateType]:
        queryset = ConsolePortTemplateType.__strawberry_django_definition__.model.objects.all()
        queryset = ConsolePortTemplateType.get_queryset(queryset, info)
        return list_resolver(info, queryset, filters)

    console_server_port: ConsoleServerPortType = strawberry_django.field()

    @strawberry_django.field(field_cls=CustomStrawberryDjangoField)
    def console_server_port_list(
        self, info: Info, filters: ConsoleServerPortFilter | None = strawberry.UNSET
    ) -> List[ConsoleServerPortType]:
        queryset = ConsoleServerPortType.__strawberry_django_definition__.model.objects.all()
        queryset = ConsoleServerPortType.get_queryset(queryset, info)
        return list_resolver(info, queryset, filters)

    console_server_port_template: ConsoleServerPortTemplateType = strawberry_django.field()

    @strawberry_django.field(field_cls=CustomStrawberryDjangoField)
    def console_server_port_template_list(
        self, info: Info, filters: ConsoleServerPortTemplateFilter | None = strawberry.UNSET
    ) -> List[ConsoleServerPortTemplateType]:
        queryset = ConsoleServerPortTemplateType.__strawberry_django_definition__.model.objects.all()
        queryset = ConsoleServerPortTemplateType.get_queryset(queryset, info)
        return list_resolver(info, queryset, filters)

    device: DeviceType = strawberry_django.field()

    @strawberry_django.field(field_cls=CustomStrawberryDjangoField)
    def device_list(self, info: Info, filters: DeviceFilter | None = strawberry.UNSET) -> List[DeviceType]:
        queryset = DeviceType.__strawberry_django_definition__.model.objects.all()
        queryset = DeviceType.get_queryset(queryset, info)
        return list_resolver(info, queryset, filters)

    device_bay: DeviceBayType = strawberry_django.field()

    @strawberry_django.field(field_cls=CustomStrawberryDjangoField)
    def device_bay_list(self, info: Info, filters: DeviceBayFilter | None = strawberry.UNSET) -> List[DeviceBayType]:
        queryset = DeviceBayType.__strawberry_django_definition__.model.objects.all()
        queryset = DeviceBayType.get_queryset(queryset, info)
        return list_resolver(info, queryset, filters)

    device_bay_template: DeviceBayTemplateType = strawberry_django.field()

    @strawberry_django.field(field_cls=CustomStrawberryDjangoField)
    def device_bay_template_list(
        self, info: Info, filters: DeviceBayTemplateFilter | None = strawberry.UNSET
    ) -> List[DeviceBayTemplateType]:
        queryset = DeviceBayTemplateType.__strawberry_django_definition__.model.objects.all()
        queryset = DeviceBayTemplateType.get_queryset(queryset, info)
        return list_resolver(info, queryset, filters)

    device_role: DeviceRoleType = strawberry_django.field()

    @strawberry_django.field(field_cls=CustomStrawberryDjangoField)
    def device_role_list(self, info: Info, filters: DeviceRoleFilter | None = strawberry.UNSET) -> List[DeviceRoleType]:
        queryset = DeviceRoleType.__strawberry_django_definition__.model.objects.all()
        queryset = DeviceRoleType.get_queryset(queryset, info)
        return list_resolver(info, queryset, filters)

    device_type: DeviceTypeType = strawberry_django.field()

    @strawberry_django.field(field_cls=CustomStrawberryDjangoField)
    def device_type_list(self, info: Info, filters: DeviceTypeFilter | None = strawberry.UNSET) -> List[DeviceTypeType]:
        queryset = DeviceTypeType.__strawberry_django_definition__.model.objects.all()
        queryset = DeviceTypeType.get_queryset(queryset, info)
        return list_resolver(info, queryset, filters)

    front_port: FrontPortType = strawberry_django.field()

    @strawberry_django.field(field_cls=CustomStrawberryDjangoField)
    def front_port_list(self, info: Info, filters: FrontPortFilter | None = strawberry.UNSET) -> List[FrontPortType]:
        queryset = FrontPortType.__strawberry_django_definition__.model.objects.all()
        queryset = FrontPortType.get_queryset(queryset, info)
        return list_resolver(info, queryset, filters)

    front_port_template: FrontPortTemplateType = strawberry_django.field()

    @strawberry_django.field(field_cls=CustomStrawberryDjangoField)
    def front_port_template_list(
        self, info: Info, filters: FrontPortTemplateFilter | None = strawberry.UNSET
    ) -> List[FrontPortTemplateType]:
        queryset = FrontPortTemplateType.__strawberry_django_definition__.model.objects.all()
        queryset = FrontPortTemplateType.get_queryset(queryset, info)
        return list_resolver(info, queryset, filters)

    mac_address: MACAddressType = strawberry_django.field()

    @strawberry_django.field(field_cls=CustomStrawberryDjangoField)
    def mac_address_list(self, info: Info, filters: MACAddressFilter | None = strawberry.UNSET) -> List[MACAddressType]:
        queryset = MACAddressType.__strawberry_django_definition__.model.objects.all()
        queryset = MACAddressType.get_queryset(queryset, info)
        return list_resolver(info, queryset, filters)

    interface: InterfaceType = strawberry_django.field()

    @strawberry_django.field(field_cls=CustomStrawberryDjangoField)
    def interface_list(self, info: Info, filters: InterfaceFilter | None = strawberry.UNSET) -> List[InterfaceType]:
        queryset = InterfaceType.__strawberry_django_definition__.model.objects.all()
        queryset = InterfaceType.get_queryset(queryset, info)
        return list_resolver(info, queryset, filters)

    interface_template: InterfaceTemplateType = strawberry_django.field()

    @strawberry_django.field(field_cls=CustomStrawberryDjangoField)
    def interface_template_list(
        self, info: Info, filters: InterfaceTemplateFilter | None = strawberry.UNSET
    ) -> List[InterfaceTemplateType]:
        queryset = InterfaceTemplateType.__strawberry_django_definition__.model.objects.all()
        queryset = InterfaceTemplateType.get_queryset(queryset, info)
        return list_resolver(info, queryset, filters)

    inventory_item: InventoryItemType = strawberry_django.field()

    @strawberry_django.field(field_cls=CustomStrawberryDjangoField)
    def inventory_item_list(
        self, info: Info, filters: InventoryItemFilter | None = strawberry.UNSET
    ) -> List[InventoryItemType]:
        queryset = InventoryItemType.__strawberry_django_definition__.model.objects.all()
        queryset = InventoryItemType.get_queryset(queryset, info)
        return list_resolver(info, queryset, filters)

    inventory_item_role: InventoryItemRoleType = strawberry_django.field()

    @strawberry_django.field(field_cls=CustomStrawberryDjangoField)
    def inventory_item_role_list(
        self, info: Info, filters: InventoryItemRoleFilter | None = strawberry.UNSET
    ) -> List[InventoryItemRoleType]:
        queryset = InventoryItemRoleType.__strawberry_django_definition__.model.objects.all()
        queryset = InventoryItemRoleType.get_queryset(queryset, info)
        return list_resolver(info, queryset, filters)

    inventory_item_template: InventoryItemTemplateType = strawberry_django.field()

    @strawberry_django.field(field_cls=CustomStrawberryDjangoField)
    def inventory_item_template_list(
        self, info: Info, filters: InventoryItemTemplateFilter | None = strawberry.UNSET
    ) -> List[InventoryItemTemplateType]:
        queryset = InventoryItemTemplateType.__strawberry_django_definition__.model.objects.all()
        queryset = InventoryItemTemplateType.get_queryset(queryset, info)
        return list_resolver(info, queryset, filters)

    location: LocationType = strawberry_django.field()

    @strawberry_django.field(field_cls=CustomStrawberryDjangoField)
    def location_list(self, info: Info, filters: LocationFilter | None = strawberry.UNSET) -> List[LocationType]:
        queryset = LocationType.__strawberry_django_definition__.model.objects.all()
        queryset = LocationType.get_queryset(queryset, info)
        return list_resolver(info, queryset, filters)

    manufacturer: ManufacturerType = strawberry_django.field()

    @strawberry_django.field(field_cls=CustomStrawberryDjangoField)
    def manufacturer_list(
        self, info: Info, filters: ManufacturerFilter | None = strawberry.UNSET
    ) -> List[ManufacturerType]:
        queryset = ManufacturerType.__strawberry_django_definition__.model.objects.all()
        queryset = ManufacturerType.get_queryset(queryset, info)
        return list_resolver(info, queryset, filters)

    module: ModuleType = strawberry_django.field()

    @strawberry_django.field(field_cls=CustomStrawberryDjangoField)
    def module_list(self, info: Info, filters: ModuleFilter | None = strawberry.UNSET) -> List[ModuleType]:
        queryset = ModuleType.__strawberry_django_definition__.model.objects.all()
        queryset = ModuleType.get_queryset(queryset, info)
        return list_resolver(info, queryset, filters)

    module_bay: ModuleBayType = strawberry_django.field()

    @strawberry_django.field(field_cls=CustomStrawberryDjangoField)
    def module_bay_list(self, info: Info, filters: ModuleBayFilter | None = strawberry.UNSET) -> List[ModuleBayType]:
        queryset = ModuleBayType.__strawberry_django_definition__.model.objects.all()
        queryset = ModuleBayType.get_queryset(queryset, info)
        return list_resolver(info, queryset, filters)

    module_bay_template: ModuleBayTemplateType = strawberry_django.field()

    @strawberry_django.field(field_cls=CustomStrawberryDjangoField)
    def module_bay_template_list(
        self, info: Info, filters: ModuleBayTemplateFilter | None = strawberry.UNSET
    ) -> List[ModuleBayTemplateType]:
        queryset = ModuleBayTemplateType.__strawberry_django_definition__.model.objects.all()
        queryset = ModuleBayTemplateType.get_queryset(queryset, info)
        return list_resolver(info, queryset, filters)

    module_type: ModuleTypeType = strawberry_django.field()

    @strawberry_django.field(field_cls=CustomStrawberryDjangoField)
    def module_type_list(self, info: Info, filters: ModuleTypeFilter | None = strawberry.UNSET) -> List[ModuleTypeType]:
        queryset = ModuleTypeType.__strawberry_django_definition__.model.objects.all()
        queryset = ModuleTypeType.get_queryset(queryset, info)
        return list_resolver(info, queryset, filters)

    platform: PlatformType = strawberry_django.field()

    @strawberry_django.field(field_cls=CustomStrawberryDjangoField)
    def platform_list(self, info: Info, filters: PlatformFilter | None = strawberry.UNSET) -> List[PlatformType]:
        queryset = PlatformType.__strawberry_django_definition__.model.objects.all()
        queryset = PlatformType.get_queryset(queryset, info)
        return list_resolver(info, queryset, filters)

    power_feed: PowerFeedType = strawberry_django.field()

    @strawberry_django.field(field_cls=CustomStrawberryDjangoField)
    def power_feed_list(self, info: Info, filters: PowerFeedFilter | None = strawberry.UNSET) -> List[PowerFeedType]:
        queryset = PowerFeedType.__strawberry_django_definition__.model.objects.all()
        queryset = PowerFeedType.get_queryset(queryset, info)
        return list_resolver(info, queryset, filters)

    power_outlet: PowerOutletType = strawberry_django.field()

    @strawberry_django.field(field_cls=CustomStrawberryDjangoField)
    def power_outlet_list(
        self, info: Info, filters: PowerOutletFilter | None = strawberry.UNSET
    ) -> List[PowerOutletType]:
        queryset = PowerOutletType.__strawberry_django_definition__.model.objects.all()
        queryset = PowerOutletType.get_queryset(queryset, info)
        return list_resolver(info, queryset, filters)

    power_outlet_template: PowerOutletTemplateType = strawberry_django.field()

    @strawberry_django.field(field_cls=CustomStrawberryDjangoField)
    def power_outlet_template_list(
        self, info: Info, filters: PowerOutletTemplateFilter | None = strawberry.UNSET
    ) -> List[PowerOutletTemplateType]:
        queryset = PowerOutletTemplateType.__strawberry_django_definition__.model.objects.all()
        queryset = PowerOutletTemplateType.get_queryset(queryset, info)
        return list_resolver(info, queryset, filters)

    power_panel: PowerPanelType = strawberry_django.field()

    @strawberry_django.field(field_cls=CustomStrawberryDjangoField)
    def power_panel_list(self, info: Info, filters: PowerPanelFilter | None = strawberry.UNSET) -> List[PowerPanelType]:
        queryset = PowerPanelType.__strawberry_django_definition__.model.objects.all()
        queryset = PowerPanelType.get_queryset(queryset, info)
        return list_resolver(info, queryset, filters)

    power_port: PowerPortType = strawberry_django.field()

    @strawberry_django.field(field_cls=CustomStrawberryDjangoField)
    def power_port_list(self, info: Info, filters: PowerPortFilter | None = strawberry.UNSET) -> List[PowerPortType]:
        queryset = PowerPortType.__strawberry_django_definition__.model.objects.all()
        queryset = PowerPortType.get_queryset(queryset, info)
        return list_resolver(info, queryset, filters)

    power_port_template: PowerPortTemplateType = strawberry_django.field()

    @strawberry_django.field(field_cls=CustomStrawberryDjangoField)
    def power_port_template_list(
        self, info: Info, filters: PowerPortTemplateFilter | None = strawberry.UNSET
    ) -> List[PowerPortTemplateType]:
        queryset = PowerPortTemplateType.__strawberry_django_definition__.model.objects.all()
        queryset = PowerPortTemplateType.get_queryset(queryset, info)
        return list_resolver(info, queryset, filters)

    rack: RackType = strawberry_django.field()

    @strawberry_django.field(field_cls=CustomStrawberryDjangoField)
    def rack_list(self, info: Info, filters: RackFilter | None = strawberry.UNSET) -> List[RackType]:
        queryset = RackType.__strawberry_django_definition__.model.objects.all()
        queryset = RackType.get_queryset(queryset, info)
        return list_resolver(info, queryset, filters)

    rack_reservation: RackReservationType = strawberry_django.field()

    @strawberry_django.field(field_cls=CustomStrawberryDjangoField)
    def rack_reservation_list(
        self, info: Info, filters: RackReservationFilter | None = strawberry.UNSET
    ) -> List[RackReservationType]:
        queryset = RackReservationType.__strawberry_django_definition__.model.objects.all()
        queryset = RackReservationType.get_queryset(queryset, info)
        return list_resolver(info, queryset, filters)

    rack_role: RackRoleType = strawberry_django.field()

    @strawberry_django.field(field_cls=CustomStrawberryDjangoField)
    def rack_role_list(self, info: Info, filters: RackRoleFilter | None = strawberry.UNSET) -> List[RackRoleType]:
        queryset = RackRoleType.__strawberry_django_definition__.model.objects.all()
        queryset = RackRoleType.get_queryset(queryset, info)
        return list_resolver(info, queryset, filters)

    rack_type: RackTypeType = strawberry_django.field()

    @strawberry_django.field(field_cls=CustomStrawberryDjangoField)
    def rack_type_list(self, info: Info, filters: RackTypeFilter | None = strawberry.UNSET) -> List[RackTypeType]:
        queryset = RackTypeType.__strawberry_django_definition__.model.objects.all()
        queryset = RackTypeType.get_queryset(queryset, info)
        return list_resolver(info, queryset, filters)

    rear_port: RearPortType = strawberry_django.field()

    @strawberry_django.field(field_cls=CustomStrawberryDjangoField)
    def rear_port_list(self, info: Info, filters: RearPortFilter | None = strawberry.UNSET) -> List[RearPortType]:
        queryset = RearPortType.__strawberry_django_definition__.model.objects.all()
        queryset = RearPortType.get_queryset(queryset, info)
        return list_resolver(info, queryset, filters)

    rear_port_template: RearPortTemplateType = strawberry_django.field()

    @strawberry_django.field(field_cls=CustomStrawberryDjangoField)
    def rear_port_template_list(
        self, info: Info, filters: RearPortTemplateFilter | None = strawberry.UNSET
    ) -> List[RearPortTemplateType]:
        queryset = RearPortTemplateType.__strawberry_django_definition__.model.objects.all()
        queryset = RearPortTemplateType.get_queryset(queryset, info)
        return list_resolver(info, queryset, filters)

    region: RegionType = strawberry_django.field()

    @strawberry_django.field(field_cls=CustomStrawberryDjangoField)
    def region_list(self, info: Info, filters: RegionFilter | None = strawberry.UNSET) -> List[RegionType]:
        queryset = RegionType.__strawberry_django_definition__.model.objects.all()
        queryset = RegionType.get_queryset(queryset, info)
        return list_resolver(info, queryset, filters)

    site: SiteType = strawberry_django.field()

    @strawberry_django.field(field_cls=CustomStrawberryDjangoField)
    def site_list(self, info: Info, filters: SiteFilter | None = strawberry.UNSET) -> List[SiteType]:
        queryset = SiteType.__strawberry_django_definition__.model.objects.all()
        queryset = SiteType.get_queryset(queryset, info)
        return list_resolver(info, queryset, filters)

    site_group: SiteGroupType = strawberry_django.field()

    @strawberry_django.field(field_cls=CustomStrawberryDjangoField)
    def site_group_list(self, info: Info, filters: SiteGroupFilter | None = strawberry.UNSET) -> List[SiteGroupType]:
        queryset = SiteGroupType.__strawberry_django_definition__.model.objects.all()
        queryset = SiteGroupType.get_queryset(queryset, info)
        return list_resolver(info, queryset, filters)

    virtual_chassis: VirtualChassisType = strawberry_django.field()

    @strawberry_django.field(field_cls=CustomStrawberryDjangoField)
    def virtual_chassis_list(
        self, info: Info, filters: VirtualChassisFilter | None = strawberry.UNSET
    ) -> List[VirtualChassisType]:
        queryset = VirtualChassisType.__strawberry_django_definition__.model.objects.all()
        queryset = VirtualChassisType.get_queryset(queryset, info)
        return list_resolver(info, queryset, filters)

    virtual_device_context: VirtualDeviceContextType = strawberry_django.field()

    @strawberry_django.field(field_cls=CustomStrawberryDjangoField)
    def virtual_device_context_list(
        self, info: Info, filters: VirtualDeviceContextFilter | None = strawberry.UNSET
    ) -> List[VirtualDeviceContextType]:
        queryset = VirtualDeviceContextType.__strawberry_django_definition__.model.objects.all()
        queryset = VirtualDeviceContextType.get_queryset(queryset, info)
        return list_resolver(info, queryset, filters)
