from django.apps import AppConfig
from django.core.cache import cache
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver


class WebsiteConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "website"
    verbose_name = "Интерфейс"

