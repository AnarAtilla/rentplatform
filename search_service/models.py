from django.db import models
from property_service.models import Property
from user_service.models import User


class SearchHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='search_search_history')
    keyword = models.CharField(max_length=255)
    search_count = models.PositiveIntegerField(default=1)
    last_searched_at = models.DateTimeField(auto_now=True, verbose_name='Последний поиск')

    def __str__(self):
        return f"{self.keyword} - {self.search_count} раз"


class ViewHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='search_view_history')
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='search_viewed_properties')
    view_count = models.PositiveIntegerField(default=1, verbose_name='Количество просмотров')
    last_viewed_at = models.DateTimeField(auto_now=True, verbose_name='Последний просмотр')

    def __str__(self):
        return f"{self.property.title} - {self.view_count} просмотров"


class SearchAnalytics(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='search_search_analytics')
    search_term = models.CharField(max_length=255, verbose_name='Поисковый запрос')
    filters_applied = models.JSONField(blank=True, null=True, verbose_name='Применённые фильтры')
    results_count = models.IntegerField(default=0, verbose_name='Количество найденных объектов')
    search_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата поиска')

    def __str__(self):
        return f'Поиск: {self.search_term} (Пользователь: {self.user.email if this.user else "Аноним"})'


class PropertyViewAnalytics(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='search_view_analytics')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='search_property_views')
    view_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата просмотра')

    def __str__(self):
        return f'Просмотр: {self.property.title} (Пользователь: {self.user.email if self.user else "Аноним"})'
