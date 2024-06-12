from django.core.exceptions import ValidationError
from django.db import models


class Specialist(models.Model):
    IMPORT_DIRECTORY = "media/import/photos"

    name = models.CharField(
        max_length=300,
        verbose_name="ФИО",
    )
    job = models.CharField(
        max_length=300,
        verbose_name="должность",
    )
    experience = models.CharField(
        max_length=300,
        verbose_name="стаж",
        help_text="Продолжите фразу: Опыт работы ...",
    )
    photo = models.ImageField(
        upload_to=IMPORT_DIRECTORY,
        verbose_name="фото",
    )
    carousel_photo = models.ImageField(
        upload_to=IMPORT_DIRECTORY,
        verbose_name="фото для карусели",
        null=True,
        blank=True,
    )
    in_carousel = models.BooleanField(
        verbose_name="отображать в карусели",
        default=True,
    )
    about = models.TextField(
        verbose_name="описание опыта специалиста",
    )

    class Meta:
        verbose_name = "специалист"
        verbose_name_plural = "специалисты"

    def __str__(self) -> str:
        return f"{self.name}"

    def clean(self) -> None:
        limit_size = 5 * 1024 * 1024
        if self.photo and self.photo.size > limit_size:
            msg = f"Файл превышает допустимый размер ({limit_size})"
            raise ValidationError(msg)
