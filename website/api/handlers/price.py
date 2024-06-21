from rest_framework.mixins import ListModelMixin
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from website.api.serializers.price import PriceFileSerializer, PriceSectionSerializer
from website.models import PriceFile, PriceSection


class PriceAPI(ListModelMixin, GenericViewSet):
    serializer_class = PriceSectionSerializer
    queryset = PriceSection.objects.all().prefetch_related("prices")

    def list(self, request: Request, *args, **kwargs) -> Response:  # noqa: ARG002
        queryset = self.filter_queryset(self.get_queryset())

        serializer = self.get_serializer(queryset, many=True)
        result_dict = {
            "prices": serializer.data,
        } | PriceFileSerializer(PriceFile.objects.get(), context={"request": request}).data

        return Response(result_dict)
