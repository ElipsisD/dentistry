from django.contrib import admin
from django.utils.safestring import mark_safe

from website.models import Service


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("title",)
    list_display_links = ("title",)
    readonly_fields = ("display_photo_1", "display_photo_2")
    search_fields = ("title", "about")
    fields = (
        "title",
        "about",
        "photo_1",
        "display_photo_1",
        "main_directions",
        "photo_2",
        "display_photo_2",
    )

    @admin.display(description="миниатюра фото №1")
    def display_photo_1(self, obj: Service) -> str:
        return mark_safe(f'<img src="{obj.photo_1.url}" height={200} />')  # noqa: S308

    @admin.display(description="миниатюра фото №2")
    def display_photo_2(self, obj: Service) -> str:
        return mark_safe(f'<img src="{obj.photo_2.url}" height={200} />')  # noqa: S308
