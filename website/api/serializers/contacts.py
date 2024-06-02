from rest_framework import serializers

from website.models import Contacts


class ContactsSerializer(serializers.ModelSerializer):
    phone_number = serializers.SerializerMethodField()

    class Meta:
        model = Contacts
        exclude = ("id",)

    @staticmethod
    def get_phone_number(instance: Contacts) -> str:
        return instance.phone_number.as_international
