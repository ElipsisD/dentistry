from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet

from website.api.serializers.service import ServiceSerializer
from website.models import Service


class ServiceAPI(RetrieveModelMixin, ListModelMixin, GenericViewSet):
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()
