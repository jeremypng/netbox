from typing import List

import strawberry
import strawberry_django
from strawberry.types import Info

from .types import *
from .filters import *
from netbox.graphql.resolvers import list_resolver


@strawberry.type(name='Query')
class ExtrasQuery:
    config_context: ConfigContextType = strawberry_django.field()

    @strawberry_django.field
    def config_context_list(
        self, info: Info, filters: ConfigContextFilter | None = strawberry.UNSET
    ) -> List[ConfigContextType]:
        queryset = ConfigContextType.__strawberry_django_definition__.model.objects.all()
        queryset = ConfigContextType.get_queryset(queryset, info)
        return list_resolver(info, queryset, filters)

    config_template: ConfigTemplateType = strawberry_django.field()

    @strawberry_django.field
    def config_template_list(
        self, info: Info, filters: ConfigTemplateFilter | None = strawberry.UNSET
    ) -> List[ConfigTemplateType]:
        queryset = ConfigTemplateType.__strawberry_django_definition__.model.objects.all()
        queryset = ConfigTemplateType.get_queryset(queryset, info)
        return list_resolver(info, queryset, filters)

    custom_field: CustomFieldType = strawberry_django.field()

    @strawberry_django.field
    def custom_field_list(
        self, info: Info, filters: CustomFieldFilter | None = strawberry.UNSET
    ) -> List[CustomFieldType]:
        queryset = CustomFieldType.__strawberry_django_definition__.model.objects.all()
        queryset = CustomFieldType.get_queryset(queryset, info)
        return list_resolver(info, queryset, filters)

    custom_field_choice_set: CustomFieldChoiceSetType = strawberry_django.field()

    @strawberry_django.field
    def custom_field_choice_set_list(
        self, info: Info, filters: CustomFieldChoiceSetFilter | None = strawberry.UNSET
    ) -> List[CustomFieldChoiceSetType]:
        queryset = CustomFieldChoiceSetType.__strawberry_django_definition__.model.objects.all()
        queryset = CustomFieldChoiceSetType.get_queryset(queryset, info)
        return list_resolver(info, queryset, filters)

    custom_link: CustomLinkType = strawberry_django.field()

    @strawberry_django.field
    def custom_link_list(self, info: Info, filters: CustomLinkFilter | None = strawberry.UNSET) -> List[CustomLinkType]:
        queryset = CustomLinkType.__strawberry_django_definition__.model.objects.all()
        queryset = CustomLinkType.get_queryset(queryset, info)
        return list_resolver(info, queryset, filters)

    export_template: ExportTemplateType = strawberry_django.field()

    @strawberry_django.field
    def export_template_list(
        self, info: Info, filters: ExportTemplateFilter | None = strawberry.UNSET
    ) -> List[ExportTemplateType]:
        queryset = ExportTemplateType.__strawberry_django_definition__.model.objects.all()
        queryset = ExportTemplateType.get_queryset(queryset, info)
        return list_resolver(info, queryset, filters)

    image_attachment: ImageAttachmentType = strawberry_django.field()

    @strawberry_django.field
    def image_attachment_list(
        self, info: Info, filters: ImageAttachmentFilter | None = strawberry.UNSET
    ) -> List[ImageAttachmentType]:
        queryset = ImageAttachmentType.__strawberry_django_definition__.model.objects.all()
        queryset = ImageAttachmentType.get_queryset(queryset, info)
        return list_resolver(info, queryset, filters)

    saved_filter: SavedFilterType = strawberry_django.field()

    @strawberry_django.field
    def saved_filter_list(
        self, info: Info, filters: SavedFilterFilter | None = strawberry.UNSET
    ) -> List[SavedFilterType]:
        queryset = SavedFilterType.__strawberry_django_definition__.model.objects.all()
        queryset = SavedFilterType.get_queryset(queryset, info)
        return list_resolver(info, queryset, filters)

    journal_entry: JournalEntryType = strawberry_django.field()

    @strawberry_django.field
    def journal_entry_list(
        self, info: Info, filters: JournalEntryFilter | None = strawberry.UNSET
    ) -> List[JournalEntryType]:
        queryset = JournalEntryType.__strawberry_django_definition__.model.objects.all()
        queryset = JournalEntryType.get_queryset(queryset, info)
        return list_resolver(info, queryset, filters)

    notification: NotificationType = strawberry_django.field()

    @strawberry_django.field
    def notification_list(self, info: Info, filters: None = strawberry.UNSET) -> List[NotificationType]:
        queryset = NotificationType.__strawberry_django_definition__.model.objects.all()
        queryset = NotificationType.get_queryset(queryset, info)
        return list_resolver(info, queryset, filters)

    notification_group: NotificationGroupType = strawberry_django.field()

    @strawberry_django.field
    def notification_group_list(
        self, info: Info, filters: NotificationGroupFilter | None = strawberry.UNSET
    ) -> List[NotificationGroupType]:
        queryset = NotificationGroupType.__strawberry_django_definition__.model.objects.all()
        queryset = NotificationGroupType.get_queryset(queryset, info)
        return list_resolver(info, queryset, filters)

    subscription: SubscriptionType = strawberry_django.field()

    @strawberry_django.field
    def subscription_list(self, info: Info, filters: None = strawberry.UNSET) -> List[SubscriptionType]:
        queryset = SubscriptionType.__strawberry_django_definition__.model.objects.all()
        queryset = SubscriptionType.get_queryset(queryset, info)
        return list_resolver(info, queryset, filters)

    tag: TagType = strawberry_django.field()

    @strawberry_django.field
    def tag_list(self, info: Info, filters: TagFilter | None = strawberry.UNSET) -> List[TagType]:
        queryset = TagType.__strawberry_django_definition__.model.objects.all()
        queryset = TagType.get_queryset(queryset, info)
        return list_resolver(info, queryset, filters)

    webhook: WebhookType = strawberry_django.field()

    @strawberry_django.field
    def webhook_list(self, info: Info, filters: WebhookFilter | None = strawberry.UNSET) -> List[WebhookType]:
        queryset = WebhookType.__strawberry_django_definition__.model.objects.all()
        queryset = WebhookType.get_queryset(queryset, info)
        return list_resolver(info, queryset, filters)

    event_rule: EventRuleType = strawberry_django.field()

    @strawberry_django.field
    def event_rule_list(self, info: Info, filters: EventRuleFilter | None = strawberry.UNSET) -> List[EventRuleType]:
        queryset = EventRuleType.__strawberry_django_definition__.model.objects.all()
        queryset = EventRuleType.get_queryset(queryset, info)
        return list_resolver(info, queryset, filters)
