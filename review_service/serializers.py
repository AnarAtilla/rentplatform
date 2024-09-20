from rest_framework import serializers
from review_service.models import Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'property', 'guest', 'rating', 'comment', 'created_at']
