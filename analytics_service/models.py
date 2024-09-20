from django.db import models
from user_service.models import User
from property_service.models import Property


class SearchAnalytics(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='analytics_search_history', verbose_name='Пользователь')
    search_term = models.CharField(max_length=255, verbose_name='Поисковый запрос')
    filters_applied = models.JSONField(blank=True, null=True, verbose_name='Применённые фильтры')
    results_count = models.IntegerField(default=0, verbose_name='Количество найденных объектов')
    search_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата поиска')

    def __str__(self):
        return f'Поисковый запрос: {self.search_term} от {self.user.email if self.user else "Аноним"}'


class PropertyViewAnalytics(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='analytics_view_analytics')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='analytics_property_views')
    view_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата просмотра')

    def __str__(self):
        return f"Просмотр объекта {self.property.title} пользователем {self.user.email if self.user else 'Аноним'}"


class PopularPropertyAnalytics(models.Model):
    property = models.OneToOneField(Property, on_delete=models.CASCADE, related_name='analytics_popularity', verbose_name='Недвижимость')
    views_count = models.IntegerField(default=0, verbose_name='Количество просмотров')
    bookings_count = models.IntegerField(default=0, verbose_name='Количество бронирований')

    def __str__(self):
        return f'{self.property.title} - {self.views_count} просмотров, {self.bookings_count} бронирований'
