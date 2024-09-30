from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticated
from .models import Booking
from .permissions import IsOwnerOrReadOnly
from .serializers import BookingSerializer
from notifications_service.utils import send_email_notification
from notifications_service.models import Notification

# Создание и просмотр списка бронирований
class BookingListCreateView(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """
        Создаем бронирование с привязкой к текущему пользователю.
        """
        serializer.save(guest=self.request.user)

    def get_queryset(self):
        """
        Возвращаем бронирования, относящиеся к текущему пользователю.
        """
        # Проверяем для Swagger-документации (фальшивый запрос, чтобы избежать ошибок при генерации схемы)
        if getattr(self, 'swagger_fake_view', False):
            return Booking.objects.none()

        if self.request.user.is_staff:
            # Администраторы могут видеть все бронирования
            return Booking.objects.all()

        # Обычные пользователи видят только свои бронирования
        return Booking.objects.filter(guest=self.request.user)


# Просмотр, обновление и удаление бронирования
class BookingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def perform_update(self, serializer):
        """
        При обновлении бронирования отправляем уведомление.
        """
        instance = serializer.save()

        # Отправляем уведомление при подтверждении бронирования
        if instance.status == 'confirmed':
            message = f'Ваше бронирование для {instance.property.title} подтверждено!'
            Notification.objects.create(
                recipient=instance.guest,
                message=message,
            )
            send_email_notification(
                'Подтверждение бронирования',
                message,
                instance.guest.email
            )


# Список бронирований для конкретного объекта недвижимости
class BookingListByPropertyView(generics.ListAPIView):
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Возвращаем бронирования для указанного объекта недвижимости.
        """
        if getattr(self, 'swagger_fake_view', False):
            return Booking.objects.none()

        # Фильтрация бронирований по конкретному объекту недвижимости
        property_id = self.kwargs['property_id']
        return Booking.objects.filter(property_id=property_id)


# Список бронирований для текущего пользователя
class BookingListByUserView(generics.ListAPIView):
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Возвращаем бронирования для текущего пользователя.
        """
        if getattr(self, 'swagger_fake_view', False):
            return Booking.objects.none()

        # Фильтрация бронирований по текущему пользователю
        return Booking.objects.filter(guest=self.request.user)
