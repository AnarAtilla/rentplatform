from rest_framework import serializers
from .models import Property

class PropertySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')

    class Meta:
        model = Property
        fields = ['id', 'title', 'description', 'location', 'price', 'owner', 'property_type', 'rooms', 'bathrooms', 'amenities', 'photos', 'created_at', 'updated_at']
