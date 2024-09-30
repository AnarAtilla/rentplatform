from django.urls import path
from .views import (
    NotificationListView,
    MarkAsReadView,
    MarkAllAsReadView,
    UnreadNotificationsListView,
    NotificationDeleteView,
    DeleteAllNotificationsView
)

urlpatterns = [
    # Список всех уведомлений для текущего пользователя
    path('notifications/', NotificationListView.as_view(), name='notification_list'),

    # Маркировка уведомления как прочитанного
    path('notifications/<int:pk>/read/', MarkAsReadView.as_view(), name='notification_read'),

    # Маркировка всех уведомлений как прочитанные
    path('notifications/mark-all-read/', MarkAllAsReadView.as_view(), name='notifications_mark_all_read'),

    # Список непрочитанных уведомлений
    path('notifications/unread/', UnreadNotificationsListView.as_view(), name='unread_notifications'),

    # Удаление одного уведомления
    path('notifications/<int:pk>/delete/', NotificationDeleteView.as_view(), name='notification_delete'),

    # Удаление всех уведомлений
    path('notifications/delete-all/', DeleteAllNotificationsView.as_view(), name='delete_all_notifications'),
]
