from django.contrib import admin

from website.models import Application


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "done")
    list_display_links = ("id", "name")
    readonly_fields = ("phone_number",)
    search_fields = ("name", "phone_number", "INN")
    list_filter = ("reporting_year", "issue_type", "done")
