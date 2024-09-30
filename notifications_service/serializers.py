from rest_framework import serializers
from .models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    recipient = serializers.ReadOnlyField(source='recipient.email')

    class Meta:
        model = Notification
        fields = ['id', 'recipient', 'message', 'created_at', 'read']
