from collections import OrderedDict
import logging
from smtplib import SMTPException

from django.core.mail import send_mail
from django.utils.html import strip_tags

from config.settings import EMAIL_HOST_USER
from core.models import Config
from website.models import Specialist
from website.models.application import IssueType
from website.models.notification import NotificationType

logger = logging.getLogger(__name__)

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


def make_email_notification(message_text: str) -> None:
    """Make notification to email chat from config."""
    recipient = Config.objects.get().email_address.strip()
    if not recipient:
        logger.warning("Skipping email notification because recipient address is empty.")
        return

    logger.info("Sending email notification to %s.", recipient)
    html_message = message_text.replace("\n", "<br>")
    plain_message = strip_tags(message_text)

    try:
        send_mail(
            "Новое уведомление!",
            plain_message,
            EMAIL_HOST_USER,
            [recipient],
            fail_silently=False,
            html_message=html_message,
        )
        logger.info("Email notification sent to %s.", recipient)
    except (OSError, SMTPException):
        logger.exception("Failed to send email notification.")


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
