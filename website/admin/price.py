from django.contrib import admin
from solo.admin import SingletonModelAdmin

from website.models import Price, PriceCategory, PriceFile


class PriceAdminInline(admin.StackedInline):
    model = Price
    extra = 1


@admin.register(PriceCategory)
class PriceCategoryAdmin(admin.ModelAdmin):
    inlines = [PriceAdminInline]  # noqa: RUF012


@admin.register(PriceFile)
class PriceFileAdmin(SingletonModelAdmin):
    ...
