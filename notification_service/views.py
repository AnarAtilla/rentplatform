from rest_framework import generics
from notification_service.models import Notification
from notification_service.serializers import NotificationSerializer

class NotificationListView(generics.ListAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
