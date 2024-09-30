from .models import PropertyView
import django_filters
from .models import SearchQuery
class PropertyViewFilter(django_filters.FilterSet):
    start_date = django_filters.DateFilter(field_name='view_date', lookup_expr='gte')
    end_date = django_filters.DateFilter(field_name='view_date', lookup_expr='lte')
    user_email = django_filters.CharFilter(field_name='user__email', lookup_expr='icontains')

    class Meta:
        model = PropertyView
        fields = ['property', 'user_email', 'start_date', 'end_date']

class SearchQueryFilter(django_filters.FilterSet):
    start_date = django_filters.DateFilter(field_name='search_date', lookup_expr='gte')
    end_date = django_filters.DateFilter(field_name='search_date', lookup_expr='lte')
    query = django_filters.CharFilter(field_name='query', lookup_expr='icontains')

    class Meta:
        model = SearchQuery
        fields = ['user', 'query', 'start_date', 'end_date']
