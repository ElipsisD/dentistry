from collections import OrderedDict

import requests
from django.core.mail import send_mail
from django.utils.html import strip_tags

from config.settings import BOT_TOKEN, EMAIL_HOST_USER
from core.models import Config
from website.models import Specialist
from website.models.notification import NotificationType

CALLBACK_TEMPLATE = """Поступил запрос на обратный звонок!\n
<b>Имя:</b> {}
<b>Телефон:</b> {}"""


FREE_CONSULTATION_TEMPLATE = """Запись на бесплатную консультацию!\n
<b>Имя:</b> {}
<b>Телефон:</b> {}
<b>Проблема:</b> {}
<b>Специалист:</b> {}"""


def make_telegram_notification(data: OrderedDict) -> None:
    """Make notification to Telegram chat from config."""
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    message_text = get_message_text(data)
    payload = {"chat_id": Config.objects.get().telegram_chat, "text": message_text, "parse_mode": "HTML"}

    requests.post(url, data=payload, timeout=60)


def make_email_notification(data: OrderedDict) -> None:
    """Make notification to email chat from config."""
    message_text = strip_tags(get_message_text(data))
    send_mail(
        "Новый запрос на обратный звонок!",
        message_text,
        EMAIL_HOST_USER,
        [Config.objects.get().email_address],
        fail_silently=False,
    )


def get_message_text(data: OrderedDict) -> str:
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
                Specialist.objects.get(pk=sp).name if (sp := data["specialist"]) else "-"
            )
