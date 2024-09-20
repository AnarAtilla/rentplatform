from rest_framework import serializers
from booking_service.models import Booking

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['property', 'guest', 'check_in', 'check_out', 'total_price', 'status']  # Убедитесь, что эти поля соответствуют вашей модели
