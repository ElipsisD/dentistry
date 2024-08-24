from django.db import models


class IssueType(models.TextChoices):
    CLINIC = "CLINIC", "Выдать в клинике"
    EMAIL = "EMAIL", "Выслать на почту"


class Application(models.Model):
    name = models.CharField(
        max_length=300,
        verbose_name="имя клиента",
        blank=True,
    )
    taxpayer_name = models.CharField(
        max_length=300,
        verbose_name="имя налогоплательщика",
        blank=True,
    )
    INN = models.CharField(
        max_length=300,
        verbose_name="ИНН налогоплательщика",
        blank=True,
    )
    reporting_year = models.PositiveSmallIntegerField(
        verbose_name="отчетный год",
        blank=True,
    )
    phone_number = models.CharField(
        max_length=300,
        verbose_name="номер телефона",
        blank=True,
    )
    issue_type = models.CharField(
        max_length=50,
        verbose_name="вариант получения",
        choices=IssueType.choices,
    )
    email = models.EmailField(
        verbose_name="email",
        blank=True,
    )
    done = models.BooleanField(
        verbose_name="подготовлено",
        default=False,
    )

    class Meta:
        verbose_name = "заявление"
        verbose_name_plural = "заявления"

    def __str__(self) -> str:
        return f"Заявление №{self.pk}"
