from django.contrib import admin
from analytics_service.models import SearchAnalytics, PopularPropertyAnalytics  # Импортируем модели

@admin.register(SearchAnalytics)
class SearchAnalyticsAdmin(admin.ModelAdmin):
    list_display = ('user', 'search_term', 'search_date', 'results_count')

@admin.register(PopularPropertyAnalytics)
class PopularPropertyAnalyticsAdmin(admin.ModelAdmin):
    list_display = ('property', 'views_count', 'bookings_count')
