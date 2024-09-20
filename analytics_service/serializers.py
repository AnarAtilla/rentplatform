from rest_framework import serializers
from analytics_service.models import SearchAnalytics, PopularPropertyAnalytics, PropertyViewAnalytics

class SearchAnalyticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SearchAnalytics
        fields = ['id', 'user', 'search_term', 'filters_applied', 'results_count', 'search_date']
        ref_name = "AnalyticsServiceSearchAnalyticsSerializer"  # Уникальное имя

class PopularPropertyAnalyticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PopularPropertyAnalytics
        fields = ['id', 'property', 'views_count', 'bookings_count']


class PropertyViewAnalyticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyViewAnalytics
        fields = ['id', 'property', 'user', 'view_date']
