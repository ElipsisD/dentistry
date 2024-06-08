from django.apps import AppConfig
from django.core.cache import cache
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver


class WebsiteConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "website"
    verbose_name = "Интерфейс"

    def ready(self) -> None:
        # Импортируем сигналы

        # Подключаем сигналы ко всем моделям
        for model in self.get_models():
            post_save.connect(clear_cache, sender=model)
            post_delete.connect(clear_cache, sender=model)


@receiver(post_save)
@receiver(post_delete)
def clear_cache(sender, **kwargs) -> None:  # noqa: ARG001, ANN001, D103
    # Очищаем кэш
    cache.clear()
