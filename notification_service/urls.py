from django.urls import path
from notification_service import views

urlpatterns = [
    path('notifications/', views.NotificationListView.as_view(), name='notifications_list'),
]
