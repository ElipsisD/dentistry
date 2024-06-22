from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet

from website.api.serializers.discount import DiscountSerializer
from website.models import Discount


class DiscountAPI(RetrieveModelMixin, ListModelMixin, GenericViewSet):
    serializer_class = DiscountSerializer
    queryset = Discount.objects.all()
