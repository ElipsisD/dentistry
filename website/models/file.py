from django.core.exceptions import ValidationError
from django.db import models


class File(models.Model):
    IMPORT_DIRECTORY = "media/import/files"

    name = models.TextField(
        verbose_name="имя файла",
    )
    file = models.FileField(
        upload_to=IMPORT_DIRECTORY,
        verbose_name="файл",
    )

    class Meta:
        verbose_name = "файл"
        verbose_name_plural = "файлы"

    def __str__(self) -> str:
        return "Файл: " + self.name

    def clean(self) -> None:
        limit_size = 10 * 1024 * 1024
        if self.file and self.file.size > limit_size:
            msg = f"Файл превышает допустимый размер ({limit_size})"
            raise ValidationError(msg)
