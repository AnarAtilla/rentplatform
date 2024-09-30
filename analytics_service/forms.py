from django import forms
from .models import PropertyView
from .models import SearchQuery
class PropertyViewForm(forms.ModelForm):
    class Meta:
        model = PropertyView
        fields = ['property', 'user', 'view_date']


class SearchQueryForm(forms.ModelForm):
    class Meta:
        model = SearchQuery
        fields = ['user', 'query', 'results_count', 'search_date']
