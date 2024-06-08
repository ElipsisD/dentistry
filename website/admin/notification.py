from django.contrib import admin

from website.models.notification import Notification


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "callback")
    list_display_links = ("id", "name")
    search_fields = ("name", "phone")
    list_filter = ("callback",)
