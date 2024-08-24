from collections import OrderedDict

import requests
from django.core.mail import send_mail

from config.settings import BOT_TOKEN, EMAIL_HOST_USER
from core.models import Config
from website.models import Specialist
from website.models.application import IssueType
from website.models.notification import NotificationType

CALLBACK_TEMPLATE = """Поступил запрос на обратный звонок!\n
<b>Имя:</b> {}
<b>Телефон:</b> {}"""

FREE_CONSULTATION_TEMPLATE = """Запись на бесплатную консультацию!\n
<b>Имя:</b> {}
<b>Телефон:</b> {}
<b>Проблема:</b> {}
<b>Специалист:</b> {}"""

FEEDBACK_TEMPLATE = """Поступил новый отзыв!\n
<b>Имя:</b> {}
<b>Телефон:</b> {}
<b>Оценка:</b> {}
<b>Отзыв:</b> {}"""

APPLICATION_TEMPLATE = """Поступила заявка на подготовку справки!\n
<b>Имя:</b> {}
<b>Имя налогоплательщика:</b> {}
<b>ИНН налогоплательщика:</b> {}
<b>Отчетный год:</b> {}
<b>Вариант получения:</b> {}
<b>Email:</b> {}
<b>Телефон:</b> {}"""


def make_telegram_notification(message_text: str) -> None:
    """Make notification to Telegram chat from config."""
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": Config.objects.get().telegram_chat, "text": message_text, "parse_mode": "HTML"}

    requests.post(url, data=payload, timeout=60)


def make_email_notification(message_text: str) -> None:
    """Make notification to email chat from config."""
    send_mail(
        "Новое уведомление!",
        message_text,
        EMAIL_HOST_USER,
        [Config.objects.get().email_address],
        fail_silently=False,
    )


def get_feedback_message_text(data: OrderedDict) -> str:
    """Return text message for notification."""
    return FEEDBACK_TEMPLATE.format(
        data["name"],
        data["phone_number"],
        data["rating"],
        data["feedback"],
    )


def get_application_message_text(data: OrderedDict) -> str:
    """Return text message for application."""
    return APPLICATION_TEMPLATE.format(
        data["name"],
        data["taxpayer_name"],
        data["INN"],
        data["reporting_year"],
        dict(IssueType.choices)[data["issue_type"]],
        data["email"],
        data["phone_number"],
    )


def get_notification_message_text(data: OrderedDict) -> str:
    """Return text message for notification."""
    match data["notification_type"]:
        case NotificationType.CALLBACK:
            return CALLBACK_TEMPLATE.format(
                data["name"],
                data["phone_number"],
            )
        case NotificationType.FREE_CONSULTATION:
            return FREE_CONSULTATION_TEMPLATE.format(
                data["name"],
                data["phone_number"],
                client_problem if (client_problem := data["client_problem"]) else "-",
                Specialist.objects.get(pk=sp).name if (sp := data["specialist"]) else "-",
            )
