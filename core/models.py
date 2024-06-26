from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from solo.models import SingletonModel


class User(AbstractUser):
    chat_id = models.PositiveIntegerField(verbose_name="идентификатор чата", null=True)
    patronymic = models.CharField(verbose_name="отчество", max_length=150, blank=True)
    username = models.CharField(
        verbose_name="username",
        max_length=150,
        unique=True,
        validators=[UnicodeUsernameValidator()],
        error_messages={"unique": "A user with that username already exists."},
    )

    class Meta:
        verbose_name = "сотрудник"
        verbose_name_plural = "сотрудники"

    def __str__(self) -> str:
        return self.get_full_name()


class Config(SingletonModel):
    telegram_chat = models.IntegerField(
        verbose_name="идентификатор Telegram чата для уведомлений",
        blank=True,
        null=True,
    )
    send_to_telegram = models.BooleanField(
        verbose_name="отправлять уведомления в Telegram",
        default=True,
    )
    email_address = models.EmailField(
        verbose_name="почта для получения уведомлений",
        blank=True,
    )
    send_to_email = models.BooleanField(
        verbose_name="отправлять уведомления на почту",
        default=True,
    )

    class Meta:
        verbose_name = "настройки уведомлений"
        verbose_name_plural = "настройки уведомлений"

    def __str__(self) -> str:
        return "Настройки уведомлений"
