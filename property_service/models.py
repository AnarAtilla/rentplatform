from django.db import models
from user_service.models import User


class Property(models.Model):
    PROPERTY_TYPES = [
        ('apartment', 'Квартира'),
        ('house', 'Дом'),
        ('room', 'Комната'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='properties')

    rooms = models.IntegerField(default=1)  # Количество комнат
    bathrooms = models.IntegerField(default=1)  # Количество ванных комнат
    property_type = models.CharField(max_length=50, choices=PROPERTY_TYPES)  # Тип недвижимости
    amenities = models.JSONField(null=True, blank=True)  # Удобства в формате JSON
    photos = models.ImageField(upload_to='property_photos/', null=True, blank=True)  # Фото недвижимости

    def __str__(self):
        return self.title
