from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from core.models import Config
from website.api.serializers.application import ApplicationSerializer
from website.models import Application
from website.utils.notification import (
    get_application_message_text,
    make_email_notification,
    make_telegram_notification,
)


class ApplicationAPI(GenericViewSet):
    serializer_class = ApplicationSerializer
    queryset = Application.objects.all()

    def create(self, request: Request, *args, **kwargs) -> Response:  # noqa: ARG002
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        if Config.objects.get().send_to_telegram:
            make_telegram_notification(get_application_message_text(serializer.data))

        if Config.objects.get().send_to_email:
            make_email_notification(get_application_message_text(serializer.data))

        return Response(serializer.data, status=status.HTTP_201_CREATED)
