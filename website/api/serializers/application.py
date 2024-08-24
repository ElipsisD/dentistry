from rest_framework import serializers

from website.models import Application


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        exclude = ("done",)
