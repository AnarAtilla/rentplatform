from django.urls import path
from booking_service import views

urlpatterns = [
    path('create/', views.BookingCreateView.as_view(), name='create_booking'),
    path('list/', views.BookingListView.as_view(), name='booking_list'),
    path('cancel/<int:pk>/', views.BookingCancelView.as_view(), name='cancel_booking'),
]
