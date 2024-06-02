from rest_framework import serializers

from website.models import Specialist


class SpecialistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialist
        fields = "__all__"
