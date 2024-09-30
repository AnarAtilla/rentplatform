from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Notification
from .serializers import NotificationSerializer

# Список уведомлений для текущего пользователя
class NotificationListView(generics.ListAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Возвращаем уведомления только для текущего пользователя.
        """
        if getattr(self, 'swagger_fake_view', False):  # Проверяем для Swagger
            return Notification.objects.none()

        return Notification.objects.filter(recipient=self.request.user)


# Маркировка уведомления как прочитанного
class MarkAsReadView(generics.UpdateAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Разрешаем пометку только для уведомлений текущего пользователя.
        """
        if getattr(self, 'swagger_fake_view', False):  # Проверяем для Swagger
            return Notification.objects.none()

        return Notification.objects.filter(recipient=self.request.user)

    def perform_update(self, serializer):
        """
        Помечаем уведомление как прочитанное.
        """
        serializer.instance.read = True
        serializer.save()

# Маркировка всех уведомлений как прочитанные
class MarkAllAsReadView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        if getattr(self, 'swagger_fake_view', False):  # Проверяем для Swagger
            return Response({"message": "Это фейковый ответ для Swagger."})

        # Метод bulk update с аргументом queryset
        Notification.objects.filter(recipient=request.user, read=False).update(read=True)
        return Response({"message": "Все уведомления помечены как прочитанные."})


# Список непрочитанных уведомлений
class UnreadNotificationsListView(generics.ListAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):  # Проверяем для Swagger
            return Notification.objects.none()

        return Notification.objects.filter(recipient=self.request.user, read=False)


# Удаление одного уведомления
class NotificationDeleteView(generics.DestroyAPIView):
    queryset = Notification.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):  # Проверяем для Swagger
            return Notification.objects.none()

        return Notification.objects.filter(recipient=self.request.user)


# Удаление всех уведомлений
class DeleteAllNotificationsView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        if getattr(self, 'swagger_fake_view', False):  # Проверяем для Swagger
            return Response({"message": "This is a fake response for Swagger."})

        Notification.objects.filter(recipient=request.user).delete()
        return Response({"message": "Все уведомления удалены."})
