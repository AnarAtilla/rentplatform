from rest_framework import serializers
from notification_service.models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['user', 'message', 'is_read', 'created_at']  # Убедитесь, что поля соответствуют вашей модели
