from django.db import models


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
