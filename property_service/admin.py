from django.contrib import admin
from .models import Property, PropertyImage

class PropertyImageInline(admin.TabularInline):
    model = PropertyImage
    extra = 1

class PropertyAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'price', 'property_type', 'owner', 'created_at')
    search_fields = ('title', 'location')
    list_filter = ('property_type', 'location', 'price')
    ordering = ('-created_at',)
    inlines = [PropertyImageInline]  # Включаем возможность добавлять изображения через админку

admin.site.register(Property, PropertyAdmin)
admin.site.register(PropertyImage)
