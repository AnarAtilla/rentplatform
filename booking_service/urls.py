from django.urls import path
from .views import BookingListCreateView, BookingDetailView, BookingListByPropertyView, BookingListByUserView

urlpatterns = [
    path('bookings/', BookingListCreateView.as_view(), name='booking_list_create'),
    path('bookings/<int:pk>/', BookingDetailView.as_view(), name='booking_detail'),
    path('property/<int:property_id>/bookings/', BookingListByPropertyView.as_view(), name='property_bookings'),
    path('my-bookings/', BookingListByUserView.as_view(), name='user_bookings'),
]
