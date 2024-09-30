from django.db import models
from django.conf import settings
from property_service.models import Property  # Assuming Property model exists in property_service

class SearchQuery(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Пользователь")
    query = models.CharField(max_length=255, verbose_name="Поисковый запрос")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата поиска")
    results_count = models.PositiveIntegerField(default=0, verbose_name="Количество найденных результатов")

    def __str__(self):
        return f'{self.user} - {self.query}'

class PropertyView(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Пользователь")
    property = models.ForeignKey(Property, on_delete=models.CASCADE, verbose_name="Недвижимость")
    viewed_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата просмотра")

    def __str__(self):
        return f'{self.user} - {self.property.title}'
