from django.contrib import admin
from .models import SearchHistory, ViewHistory, SearchAnalytics, PropertyViewAnalytics

@admin.register(SearchHistory)
class SearchHistoryAdmin(admin.ModelAdmin):
    list_display = ['user', 'keyword', 'search_count', 'last_searched_at']

@admin.register(ViewHistory)
class ViewHistoryAdmin(admin.ModelAdmin):
    list_display = ['user', 'property', 'view_count', 'last_viewed_at']

@admin.register(SearchAnalytics)
class SearchAnalyticsAdmin(admin.ModelAdmin):
    list_display = ['user', 'search_term', 'filters_applied', 'results_count', 'search_date']

@admin.register(PropertyViewAnalytics)
class PropertyViewAnalyticsAdmin(admin.ModelAdmin):
    list_display = ['user', 'property', 'view_date']
