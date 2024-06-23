from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet

from website.api.serializers.service import ServiceCarouselSerializer, ServiceSerializer
from website.models import Service


class ServiceAPI(RetrieveModelMixin, ListModelMixin, GenericViewSet):
    serializer_class = ServiceSerializer
    queryset = Service.objects.all().select_related("specialist")


class ServiceCarouselAPI(ListModelMixin, GenericViewSet):
    serializer_class = ServiceCarouselSerializer
    queryset = Service.objects.filter(in_carousel=True)
