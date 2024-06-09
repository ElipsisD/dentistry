from django.core.exceptions import ValidationError
from django.db import models
from solo.models import SingletonModel


class PriceCategory(models.Model):
    name = models.CharField(
        max_length=300,
        verbose_name="название категории",
    )

    class Meta:
        verbose_name = "категория прайс листа"
        verbose_name_plural = "категории прайс листа"

    def __str__(self) -> str:
        return f"{self.name}"


class Price(models.Model):
    category = models.ForeignKey(
        to="website.PriceCategory",
        on_delete=models.CASCADE,
        related_name="prices",
        verbose_name="категория",
    )
    name = models.TextField(
        verbose_name="название услуги",
    )
    price = models.IntegerField(
        verbose_name="цена",
    )

    class Meta:
        verbose_name = "услуга"
        verbose_name_plural = "услуги"

    def __str__(self) -> str:
        return f"{self.name[:40]}..."


class PriceFile(SingletonModel):
    IMPORT_DIRECTORY = "media/import/price"

    file = models.FileField(
        upload_to=IMPORT_DIRECTORY,
        verbose_name="файл прайс листа",
    )

    class Meta:
        verbose_name = "файл прайс листа"
        verbose_name_plural = "файлы прайс листа"

    def __str__(self) -> str:
        return "Файл прайс листа"

    def clean(self) -> None:
        limit_size = 10 * 1024 * 1024
        if self.file and self.file.size > limit_size:
            msg = f"Файл превышает допустимый размер ({limit_size})"
            raise ValidationError(msg)
