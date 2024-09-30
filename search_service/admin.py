
from django.contrib import admin
from .models import SearchQuery, PropertyView

@admin.register(SearchQuery)
class SearchQueryAdmin(admin.ModelAdmin):
    list_display = ('user', 'query', 'created_at', 'results_count')
    search_fields = ('query',)
    list_filter = ('created_at',)

@admin.register(PropertyView)
class PropertyViewAdmin(admin.ModelAdmin):
    list_display = ('user', 'property', 'viewed_at')
    search_fields = ('property__title',)
    list_filter = ('viewed_at',)
