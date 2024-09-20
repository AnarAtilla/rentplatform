from rest_framework import serializers
from analytics_service.models import PropertyViewAnalytics
from property_service.models import Property

# Serializer for PropertyViewAnalytics
class PropertyViewAnalyticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyViewAnalytics
        fields = ['id', 'property', 'user', 'view_date']

# Serializer for Property creation
class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = ['title', 'description', 'location', 'price', 'rooms', 'bathrooms', 'property_type', 'amenities', 'photos']
