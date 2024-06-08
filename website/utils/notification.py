from collections import OrderedDict

import requests
from django.core.mail import send_mail

from config.settings import BOT_TOKEN, EMAIL_HOST_USER
from core.models import Config
from website.models import Specialist

MASSAGE_TEXT_TEMPLATE = """Поступил заказ на обратный звонок!\n
<b>Имя:</b> {}
<b>Телефон:</b> {}
<b>Специалист:</b> {}"""


def make_telegram_notification(data: OrderedDict) -> None:
    """Make notification to Telegram chat from config."""
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    massage_text = MASSAGE_TEXT_TEMPLATE.format(
        data["name"],
        data["phone_number"],
        Specialist.objects.get(pk=sp).name if (sp := data["specialist"]) else "не выбран"
    )
    payload = {"chat_id": Config.objects.get().telegram_chat, "text": massage_text, "parse_mode": "HTML"}

    requests.post(url, data=payload, timeout=60)


def make_email_notification(data: OrderedDict) -> None:
    """Make notification to email chat from config."""
    massage_text = MASSAGE_TEXT_TEMPLATE.format(
        data["name"],
        data["phone_number"],
        Specialist.objects.get(pk=sp).name if (sp := data["specialist"]) else "не выбран"
    )
    send_mail(
        "Новый запрос на обратный звонок!",
        massage_text,
        EMAIL_HOST_USER,
        [Config.objects.get().email_address],
        fail_silently=False,
    )