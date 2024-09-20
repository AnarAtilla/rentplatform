from django_filters import rest_framework as filters
from analytics_service.models import PropertyViewAnalytics

class PropertyViewAnalyticsFilter(filters.FilterSet):
    property = filters.CharFilter(field_name='property__title', lookup_expr='icontains')  # Поиск по названию недвижимости
    view_date = filters.DateFromToRangeFilter()  # Фильтр по диапазону дат

    class Meta:
        model = PropertyViewAnalytics
        fields = ['property', 'view_date']
