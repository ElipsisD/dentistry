from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models


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
