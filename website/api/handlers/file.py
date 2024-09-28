from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from website.api.serializers.file import FileSerializer
from website.api.serializers.price import PriceFileSerializer, PriceSectionSerializer
from website.models import File, PriceFile, PriceSection


class FileAPI(
    ListModelMixin,
    RetrieveModelMixin,
    GenericViewSet,
):
    serializer_class = FileSerializer
    queryset = File.objects.all()

    def list(self, request: Request, *args, **kwargs) -> Response:  # noqa: ARG002
        serializer = self.get_serializer(self.queryset, many=True)
        return Response(serializer.data)
