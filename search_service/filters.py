import django_filters
from search_service.models import SearchAnalytics

class SearchAnalyticsFilter(django_filters.FilterSet):
    search_term = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = SearchAnalytics
        fields = ['search_term', 'search_date']
