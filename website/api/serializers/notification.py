from rest_framework import serializers

from website.models import Notification


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        exclude = ("callback", "note")
