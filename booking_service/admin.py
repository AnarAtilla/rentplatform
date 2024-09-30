from django.contrib import admin
from booking_service.models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['rental_property', 'guest', 'check_in', 'check_out', 'status']

    def rental_property(self, obj):
        return obj.rental_property.title
