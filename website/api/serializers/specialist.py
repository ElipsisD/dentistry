from rest_framework import serializers

from website.models import Specialist


class SpecialistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialist
        fields = (
            "id",
            "name",
            "job",
            "experience",
            "photo",
            "about",
        )


class CarouselSpecialistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialist
        fields = (
            "id",
            "name",
            "job",
            "experience",
            "carousel_photo",
            "about",
        )
