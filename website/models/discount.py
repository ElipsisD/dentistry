from django.core.exceptions import ValidationError
from django.db import models


class Discount(models.Model):
    IMPORT_DIRECTORY = "media/import/discount"

    title = models.CharField(
        max_length=300,
        verbose_name="заголовок",
    )
    validity = models.CharField(
        max_length=300,
        verbose_name="срок действия",
        blank=True,
    )
    photo = models.ImageField(
        upload_to=IMPORT_DIRECTORY,
        verbose_name="фото",
    )
    about = models.TextField(
        verbose_name="описание",
        blank=True,
    )
    note = models.TextField(
        verbose_name="примечание",
        blank=True,
    )

    class Meta:
        verbose_name = "акция"
        verbose_name_plural = "акции"

    def __str__(self) -> str:
        return f"{self.title}"

    def clean(self) -> None:
        limit_size = 5 * 1024 * 1024
        if self.photo and self.photo.size > limit_size:
            msg = f"Файл превышает допустимый размер ({limit_size})"
            raise ValidationError(msg)
