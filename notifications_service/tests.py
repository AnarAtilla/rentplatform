from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import Notification, User

class NotificationTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='user@example.com', password='password123')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_create_notification(self):
        Notification.objects.create(recipient=self.user, message="Test notification")
        response = self.client.get(reverse('notification_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_mark_notification_as_read(self):
        notification = Notification.objects.create(recipient=self.user, message="Test notification")
        response = self.client.patch(reverse('notification_read', kwargs={'pk': notification.pk}), {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        notification.refresh_from_db()
        self.assertTrue(notification.read)

    def test_mark_all_notifications_as_read(self):
        Notification.objects.create(recipient=self.user, message="Test notification 1", read=False)
        Notification.objects.create(recipient=self.user, message="Test notification 2", read=False)
        response = self.client.post(reverse('notifications_mark_all_read'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(Notification.objects.filter(read=True).count(), 2)

    def test_get_unread_notifications(self):
        Notification.objects.create(recipient=self.user, message="Test notification 1", read=False)
        Notification.objects.create(recipient=self.user, message="Test notification 2", read=True)
        response = self.client.get(reverse('unread_notifications'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_delete_notification(self):
        notification = Notification.objects.create(recipient=self.user, message="Test notification")
        response = self.client.delete(reverse('notification_delete', kwargs={'pk': notification.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Notification.objects.count(), 0)

    def test_delete_all_notifications(self):
        Notification.objects.create(recipient=self.user, message="Test notification 1")
        Notification.objects.create(recipient=self.user, message="Test notification 2")
        response = self.client.delete(reverse('delete_all_notifications'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Notification.objects.count(), 0)