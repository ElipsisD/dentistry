from rest_framework import serializers

from website.api.serializers.specialist import SpecialistSerializer
from website.models import Service


class ServiceSerializer(serializers.ModelSerializer):
    specialist = SpecialistSerializer()

    class Meta:
        model = Service
        exclude = (
            "carousel_photo",
            "in_carousel",
        )


class ServiceCarouselSerializer(serializers.ModelSerializer):

    class Meta:
        model = Service
        exclude = (
            "specialist",
            "photo_1",
            "about",
            "photo_2",
            "main_directions",
            "in_carousel",
        )
