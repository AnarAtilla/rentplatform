from django.contrib import admin
from booking_service.models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('property', 'guest', 'check_in', 'check_out', 'status')
