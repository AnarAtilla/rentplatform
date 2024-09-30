from django.contrib import admin
from .models import PropertyView, SearchQuery

@admin.register(PropertyView)
class PropertyViewAdmin(admin.ModelAdmin):
    list_display = ('property', 'user', 'view_date')
    list_filter = ('property', 'view_date')
    search_fields = ('property__title', 'user__email')

@admin.register(SearchQuery)
class SearchQueryAdmin(admin.ModelAdmin):
    list_display = ('user', 'query', 'results_count', 'search_date')
    list_filter = ('search_date',)
    search_fields = ('query', 'user__email')
