from rest_framework import serializers

from website.models import PriceFile


class FileSerializer(serializers.ModelSerializer):
    file = serializers.SerializerMethodField()

    class Meta:
        model = PriceFile
        fields = "__all__"

    def get_file(self, instance: PriceFile) -> str | None:
        request = self.context.get("request")
        if instance.file and request:
            return request.build_absolute_uri(instance.file.url)
        return None
