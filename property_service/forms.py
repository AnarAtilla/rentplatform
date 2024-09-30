from django import forms
from .models import Property


class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['title', 'description', 'location', 'price', 'property_type', 'rooms', 'bathrooms', 'amenities', 'photos']

    def clean_rooms(self):
        rooms = self.cleaned_data.get('rooms')
        if rooms <= 0:
            raise forms.ValidationError('Количество комнат должно быть положительным.')
        return rooms

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price <= 0:
            raise forms.ValidationError("Цена должна быть положительной.")
        return price
