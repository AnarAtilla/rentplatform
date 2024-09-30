from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import Property
from .models import User

class PropertyTests(TestCase):
    def setUp(self):
        # Создаем пользователя
        self.user = User.objects.create_user(email='user@example.com', password='password123')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        # Данные для нового объекта недвижимости
        self.property_data = {
            'title': 'Test Property',
            'description': 'Test description',
            'location': 'Test location',
            'price': 1000.00,
            'property_type': 'apartment',
            'rooms': 2,
            'bathrooms': 1
        }

    def test_create_property(self):
        # Тест на создание объекта недвижимости
        response = self.client.post(reverse('property_create'), self.property_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Property.objects.count(), 1)
        self.assertEqual(Property.objects.get().title, 'Test Property')

    def test_get_property_list(self):
        # Тест на получение списка объектов недвижимости
        Property.objects.create(owner=self.user, **self.property_data)
        response = self.client.get(reverse('property_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_property_detail(self):
        # Тест на получение одного объекта недвижимости
        property_instance = Property.objects.create(owner=self.user, **self.property_data)
        response = self.client.get(reverse('property_detail', kwargs={'pk': property_instance.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], property_instance.title)

    def test_update_property(self):
        # Тест на обновление объекта недвижимости
        property_instance = Property.objects.create(owner=self.user, **self.property_data)
        updated_data = self.property_data.copy()
        updated_data['title'] = 'Updated Property'
        response = self.client.put(reverse('property_edit', kwargs={'pk': property_instance.pk}), updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        property_instance.refresh_from_db()
        self.assertEqual(property_instance.title, 'Updated Property')

    def test_delete_property(self):
        # Тест на удаление объекта недвижимости
        property_instance = Property.objects.create(owner=self.user, **self.property_data)
        response = self.client.delete(reverse('property_delete', kwargs={'pk': property_instance.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Property.objects.count(), 0)
