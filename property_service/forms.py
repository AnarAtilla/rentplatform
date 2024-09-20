import forms


class PropertyViewAnalyticsForm(forms.ModelForm):
    class Meta:
        model = PropertyViewAnalytics
        fields = ['property', 'user', 'view_date']


