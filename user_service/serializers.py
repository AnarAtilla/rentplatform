from rest_framework import serializers
from .models import User

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['email', 'password', 'is_landlord', 'company_name', 'address', 'phone_number']

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            is_landlord=validated_data.get('is_landlord', False),
            company_name=validated_data.get('company_name', ''),
            address=validated_data.get('address', ''),
            phone_number=validated_data.get('phone_number', '')
        )
        return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'is_landlord', 'company_name', 'address', 'phone_number', 'additional_contact_info', 'status']
