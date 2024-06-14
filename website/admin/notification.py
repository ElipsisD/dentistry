from django.contrib import admin

from website.models.notification import Notification


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "notification_type", "callback")
    list_display_links = ("id", "name")
    readonly_fields = ("phone_number",)
    search_fields = ("name", "phone_number")
    list_filter = ("callback", "notification_type")
    fields = (
        "name",
        "phone_number",
        "client_problem",
        "notification_type",
        "specialist",
        "callback",
        "note",
    )
