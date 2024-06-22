from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from solo.models import SingletonModel


class Contacts(SingletonModel):
    phone_number = PhoneNumberField(
        verbose_name="номер телефона",
    )
    address = models.CharField(
        max_length=300,
        verbose_name="адрес",
    )
    working_hours = models.CharField(
        max_length=300,
        verbose_name="часы работы",
        help_text="для размещения информации на нескольких строках, нужно разделить строку знаком ','",
    )
    email = models.EmailField(
        verbose_name="email",
    )

    class Meta:
        verbose_name = "контакты"
        verbose_name_plural = "контакты"

    def __str__(self) -> str:
        return "Контакты"
