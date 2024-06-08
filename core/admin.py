from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from django.http import HttpRequest
from solo.admin import SingletonModelAdmin

from core.models import Config, User

admin.site.site_title = "Краевой Центр Дентальной Имплантации"
admin.site.index_title = "Административная панель"
admin.site.site_header = "КЦДИ"
admin.site.site_url = None
admin.site.unregister(Group)


@admin.register(User)
class MyUserAdmin(UserAdmin):
    list_display = (
        "pk",
        "last_name",
        "first_name",
        "patronymic",
    )
    list_display_links = (
        "pk",
        "last_name",
        "first_name",
        "patronymic",
    )

    def get_fieldsets(self, request: HttpRequest, obj=...):
        if not obj:
            return super().get_fieldsets(request, obj)
        return (
            (
                "Персональная информация",
                {
                    "fields": (
                        "first_name",
                        "last_name",
                        "patronymic",
                    )
                },
            ),
            ("Настройки", {"fields": ("username",)}),
        )

    class Meta:
        model = User


@admin.register(Config)
class ConfigAdmin(SingletonModelAdmin):
    ...
