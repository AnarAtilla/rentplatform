from booking_service.models import Booking
from booking_service.permissions import IsGuestOrReadOnly
from booking_service.serializers import BookingSerializer
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response



# API view для создания нового бронирования
class BookingCreateView(generics.CreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Создаем бронирование для текущего пользователя (гостя)
        serializer.save(guest=self.request.user)


# API view для получения списка всех бронирований пользователя
class BookingListView(generics.ListAPIView):
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Возвращаем только бронирования текущего пользователя
        return Booking.objects.filter(guest=self.request.user)


# API view для отмены бронирования
class BookingCancelView(generics.DestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated, IsGuestOrReadOnly]

    def delete(self, request, *args, **kwargs):
        booking = self.get_object()
        # Проверяем, что текущий пользователь — это гость, который сделал бронирование
        if booking.guest != request.user:
            return Response({'error': 'Вы не можете отменить это бронирование'}, status=status.HTTP_403_FORBIDDEN)
        booking.delete()
        return Response({'success': 'Бронирование отменено'}, status=status.HTTP_204_NO_CONTENT)


# Отмена бронирования через шаблон
@login_required
def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, guest=request.user)
    if request.method == "POST":
        booking.delete()
        return redirect('user_dashboard')
    return render(request, 'booking_service/cancel_booking.html', {'booking': booking})
