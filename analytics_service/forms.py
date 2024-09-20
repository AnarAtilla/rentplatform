from django import forms
from analytics_service.models import SearchAnalytics
from analytics_service.models import PopularPropertyAnalytics
from analytics_service.models import ResponseTimeAnalytics


class SearchAnalyticsForm(forms.ModelForm):
    class Meta:
        model = SearchAnalytics
        fields = ['user', 'search_term', 'filters_applied', 'results_count', 'search_date']

class PopularPropertyAnalyticsForm(forms.ModelForm):
    class Meta:
        model = PopularPropertyAnalytics
        fields = ['property', 'views_count', 'bookings_count']


class ResponseTimeAnalyticsForm(forms.ModelForm):
    class Meta:
        model = ResponseTimeAnalytics
        fields = ['search_term', 'response_time', 'search_date']
