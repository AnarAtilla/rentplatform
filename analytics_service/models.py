from django.db import models
from django.conf import settings
from property_service.models import Property

class PropertyView(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='views', verbose_name='Недвижимость')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='property_views', verbose_name='Пользователь')
    view_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата просмотра')

    def __str__(self):
        return f'Просмотр {self.property.title} пользователем {self.user.email if self.user else "аноним"}'

class SearchQuery(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='search_queries', verbose_name='Пользователь')
    query = models.CharField(max_length=255, verbose_name='Поисковый запрос')
    results_count = models.IntegerField(default=0, verbose_name='Количество найденных объектов')
    search_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата поиска')

    def __str__(self):
        return f'Поиск: {self.query} пользователем {self.user.email if self.user else "аноним"}'
