from django.contrib import admin

from website.models import Feedback


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ("name", "rating", "published", "created_date")
    list_display_links = ("name", "rating")
    readonly_fields = ("phone_number", "name")
    search_fields = ("name", "phone_number")
    list_filter = ("published", "rating")
