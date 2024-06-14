from django.db import models


class NotificationType(models.TextChoices):
    CALLBACK = "CALLBACK", "Обратный звонок"
    FREE_CONSULTATION = "FREE_CONSULTATION", "Бесплатная консультация"


class Notification(models.Model):
    name = models.CharField(
        max_length=300,
        verbose_name="имя клиента",
        blank=True,
    )
    phone_number = models.CharField(
        max_length=300,
        verbose_name="номер телефона",
        blank=True,
    )
    client_problem = models.TextField(
        verbose_name="проблема клиента",
        blank=True,
    )
    notification_type = models.CharField(
        max_length=300,
        choices=NotificationType.choices,
        verbose_name="тип уведомления",
        default=NotificationType.CALLBACK,
        blank=False,
    )
    specialist = models.ForeignKey(
        to="website.Specialist",
        on_delete=models.SET_NULL,
        related_name="notifications",
        verbose_name="специалист",
        null=True,
        blank=True,
    )
    callback = models.BooleanField(
        verbose_name="обратный звонок",
        default=False,
    )
    note = models.TextField(
        verbose_name="примечание",
        blank=True,
    )

    class Meta:
        verbose_name = "уведомление"
        verbose_name_plural = "уведомления"

    def __str__(self) -> str:
        return f"Уведомление №{self.pk}"
