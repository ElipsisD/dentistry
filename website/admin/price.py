import nested_admin
from django.contrib import admin
from solo.admin import SingletonModelAdmin

from website.models import Price, PriceCategory, PriceFile, PriceSection


class PriceAdminInline(nested_admin.NestedStackedInline):
    model = Price
    extra = 0
    fields = (
        "name",
        "price",
    )


class PriceCategoryAdminInline(nested_admin.NestedStackedInline):
    model = PriceCategory
    inlines = [PriceAdminInline]  # noqa: RUF012
    extra = 0


@admin.register(PriceSection)
class PriceSectionAdmin(nested_admin.NestedModelAdmin):
    inlines = [PriceCategoryAdminInline, PriceAdminInline]  # noqa: RUF012


@admin.register(PriceFile)
class PriceFileAdmin(SingletonModelAdmin): ...
