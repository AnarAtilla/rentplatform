from django.contrib import admin
from property_service.models import Property

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'price', 'owner')
