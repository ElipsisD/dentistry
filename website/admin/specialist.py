from django.contrib import admin
from django.utils.safestring import mark_safe

from website.models import Specialist


@admin.register(Specialist)
class SpecialistAdmin(admin.ModelAdmin):
    list_display = ("name", "job")
    list_display_links = ("name", "job")
    readonly_fields = ("display_photo",)
    search_fields = ("name",)
    fields = (
        "name",
        "job",
        "experience",
        "photo",
        "display_photo",
        "about",
    )

    @admin.display(description="миниатюра фото")
    def display_photo(self, obj: Specialist) -> str:
        return mark_safe(f'<img src="{obj.photo.url}" height={200} />')  # noqa: S308
