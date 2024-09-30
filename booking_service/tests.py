from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import Booking, Property, User

class BookingTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='guest@example.com', password='password123')
        self.owner = User.objects.create_user(email='owner@example.com', password='password123')
        self.property = Property.objects.create(
            title='Test Property',
            description='Test description',
            location='Test location',
            price=1000.00,
            owner=self.owner,
            property_type='apartment',
            rooms=2,
            bathrooms=1
        )
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.booking_data = {
            'property': self.property.id,
            'check_in': '2024-09-25',
            'check_out': '2024-09-30',
            'total_price': 500.00
        }

    def test_create_booking(self):
        response = self.client.post(reverse('booking_list_create'), self.booking_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Booking.objects.count(), 1)

    def test_get_booking_list(self):
        Booking.objects.create(property=self.property, guest=self.user, check_in='2024-09-25', check_out='2024-09-30', total_price=500.00)
        response = self.client.get(reverse('booking_list_create'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_update_booking(self):
        booking = Booking.objects.create(property=self.property, guest=self.user, check_in='2024-09-25', check_out='2024-09-30', total_price=500.00)
        updated_data = {'check_in': '2024-09-26', 'check_out': '2024-10-01'}
        response = self.client.put(reverse('booking_detail', kwargs={'pk': booking.pk}), updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        booking.refresh_from_db()
        self.assertEqual(str(booking.check_in), '2024-09-26')

    def test_delete_booking(self):
        booking = Booking.objects.create(property=self.property, guest=self.user, check_in='2024-09-25', check_out='2024-09-30', total_price=500.00)
        response = self.client.delete(reverse('booking_detail', kwargs={'pk': booking.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Booking.objects.count(), 0)

    def test_get_bookings_for_property(self):
        # Тестируем список бронирований для конкретного объекта недвижимости
        property_instance = Property.objects.create(
            title='Test Property',
            description='Test description',
            location='Test location',
            price=1000.00,
            owner=self.owner,
            property_type='apartment',
            rooms=2,
            bathrooms=1
        )
        Booking.objects.create(property=property_instance, guest=self.user, check_in='2024-09-25',
                               check_out='2024-09-30', total_price=500.00)
        response = self.client.get(reverse('property_bookings', kwargs={'property_id': property_instance.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_my_bookings(self):
        # Тестируем список бронирований для текущего пользователя
        Booking.objects.create(property=self.property, guest=self.user, check_in='2024-09-25', check_out='2024-09-30',
                               total_price=500.00)
        response = self.client.get(reverse('user_bookings'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
