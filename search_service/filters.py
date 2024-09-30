
import django_filters
from property_service.models import Property

class PropertyFilter(django_filters.FilterSet):
    class Meta:
        model = Property
        fields = ['title', 'location', 'price']
