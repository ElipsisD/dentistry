from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from website.api.serializers.contacts import ContactsSerializer
from website.models import Contacts


class ContactsAPI(GenericViewSet):
    serializer_class = ContactsSerializer
    queryset = Contacts.objects.all()

    def list(self, request: Request, *args, **kwargs) -> Response:  # noqa: ARG002
        serializer = self.get_serializer(self.queryset.get())
        return Response(serializer.data)
