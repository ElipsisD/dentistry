from django.core.exceptions import ValidationError
from django.db import models


class Service(models.Model):
    IMPORT_DIRECTORY = "media/import/service"

    title = models.CharField(
        max_length=300,
        verbose_name="заголовок",
    )
    photo_1 = models.ImageField(
        upload_to=IMPORT_DIRECTORY,
        verbose_name="фото №1",
        null=True,
        blank=True,
    )
    about = models.TextField(
        verbose_name="описание",
        blank=True,
    )
    photo_2 = models.ImageField(
        upload_to=IMPORT_DIRECTORY,
        verbose_name="фото №2",
        null=True,
        blank=True,
    )
    main_directions = models.TextField(
        verbose_name="основные направления",
        blank=True,
    )

    class Meta:
        verbose_name = "услуга"
        verbose_name_plural = "услуги"

    def __str__(self) -> str:
        return f"{self.title}"

    def clean(self) -> None:
        limit_size = 5 * 1024 * 1024
        if (self.photo_1 and self.photo_1.size > limit_size) or (self.photo_2 and self.photo_2.size > limit_size):
            msg = f"Файл превышает допустимый размер ({limit_size})"
            raise ValidationError(msg)
