from rest_framework import serializers

from website.models import Price, PriceCategory, PriceFile


class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        exclude = ("id", "category")


class PriceCategorySerializer(serializers.ModelSerializer):
    prices = PriceSerializer(many=True)

    class Meta:
        model = PriceCategory
        exclude = ("id",)


class PriceFileSerializer(serializers.ModelSerializer):
    file = serializers.SerializerMethodField()

    class Meta:
        model = PriceFile
        exclude = ("id",)

    def get_file(self, instance: PriceFile) -> str | None:
        request = self.context.get("request")
        if instance.file and request:
            return request.build_absolute_uri(instance.file.url)
        return None
