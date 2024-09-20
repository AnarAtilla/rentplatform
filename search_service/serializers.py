from rest_framework import serializers
from search_service.models import SearchAnalytics, PropertyViewAnalytics, SearchHistory, ViewHistory

class SearchHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SearchHistory
        fields = ['user', 'keyword', 'search_count', 'last_searched_at']
        ref_name = "SearchServiceSearchAnalyticsSerializer"  # Уникальное имя
class ViewHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ViewHistory
        fields = ['user', 'property', 'view_count', 'last_viewed_at']

class SearchAnalyticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SearchAnalytics
        fields = ['id', 'user', 'search_term', 'filters_applied', 'results_count', 'search_date']

class PropertyViewAnalyticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyViewAnalytics
        fields = ['id', 'property', 'user', 'view_date']
