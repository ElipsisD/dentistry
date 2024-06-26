from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet

from website.api.serializers.specialist import CarouselSpecialistSerializer, SpecialistSerializer
from website.models import Specialist


class SpecialistAPI(ListModelMixin, GenericViewSet):
    serializer_class = SpecialistSerializer
    queryset = Specialist.objects.all()


class CarouselSpecialistAPI(ListModelMixin, GenericViewSet):
    serializer_class = CarouselSpecialistSerializer
    queryset = Specialist.objects.filter(in_carousel=True)
