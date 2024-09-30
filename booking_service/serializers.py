from rest_framework import serializers
from .models import Booking

class BookingSerializer(serializers.ModelSerializer):
    guest = serializers.ReadOnlyField(source='guest.email')
    property = serializers.ReadOnlyField(source='property.title')

    class Meta:
        model = Booking
        fields = ['id', 'property', 'guest', 'check_in', 'check_out', 'total_price', 'status', 'created_at', 'updated_at']
        read_only_fields = ['status', 'created_at', 'updated_at']

    def validate(self, data):
        if data['check_in'] >= data['check_out']:
            raise serializers.ValidationError("Дата выезда должна быть позже даты заезда.")
        return data
