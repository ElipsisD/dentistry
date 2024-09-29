from rest_framework import serializers

from website.models import File


class FileSerializer(serializers.ModelSerializer):
    file = serializers.SerializerMethodField()

    class Meta:
        model = File
        fields = "__all__"

    def get_file(self, instance: File) -> str | None:
        request = self.context.get("request")
        if instance.file and request:
            return request.build_absolute_uri(instance.file.url)
        return None
