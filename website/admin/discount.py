from django.contrib import admin
from django.utils.safestring import mark_safe

from website.models import Discount


@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    list_display = ("title",)
    list_display_links = ("title",)
    readonly_fields = ("display_photo",)
    search_fields = ("title",)
    fields = (
        "title",
        "validity",
        "photo",
        "display_photo",
        "about",
        "note",
    )

    @admin.display(description="миниатюра фото")
    def display_photo(self, obj: Discount) -> str:
        return mark_safe(f'<img src="{obj.photo.url}" height={200} />')  # noqa: S308
