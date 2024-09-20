from django_filters import rest_framework as filters
from analytics_service.models import SearchAnalytics, PopularPropertyAnalytics

class SearchAnalyticsFilter(filters.FilterSet):
    search_term = filters.CharFilter(lookup_expr='icontains')
    search_date = filters.DateFromToRangeFilter()

    class Meta:
        model = SearchAnalytics
        fields = ['search_term', 'search_date']

class PopularPropertyAnalyticsFilter(filters.FilterSet):
    views_count = filters.RangeFilter()
    bookings_count = filters.RangeFilter()

    class Meta:
        model = PopularPropertyAnalytics
        fields = ['views_count', 'bookings_count']
