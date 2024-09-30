from rest_framework import serializers
from .models import PropertyView
from .models import SearchQuery


class PropertyViewSerializer(serializers.ModelSerializer):
    property = serializers.ReadOnlyField(source='property.title')
    user = serializers.ReadOnlyField(source='user.email')

    class Meta:
        model = PropertyView
        fields = ['property', 'user', 'view_date']

class SearchQuerySerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.email')

    class Meta:
        model = SearchQuery
        fields = ['user', 'query', 'results_count', 'search_date']
