from django.db import models


class FeedbackRating(models.IntegerChoices):
    ONE = 1, "1"
    TWO = 2, "2"
    THREE = 3, "3"
    FOUR = 4, "4"
    FIVE = 5, "5"


class Feedback(models.Model):
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
    feedback = models.TextField(
        verbose_name="отзыв",
    )
    published = models.BooleanField(
        verbose_name="опубликовано",
        default=False,
    )
    rating = models.IntegerField(
        verbose_name="оценка",
        choices=FeedbackRating.choices,
    )
    created_date = models.DateTimeField(
        verbose_name="дата создания",
        auto_now_add=True,
    )

    class Meta:
        verbose_name = "отзыв"
        verbose_name_plural = "отзывы"

    def __str__(self) -> str:
        return f"Отзыв №{self.pk}"
