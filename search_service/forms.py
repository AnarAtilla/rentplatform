from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm as DjangoPasswordChangeForm

class PasswordChangeForm(DjangoPasswordChangeForm):
    class Meta:
        fields = ['old_password', 'new_password1', 'new_password2']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']  # Выберите нужные поля для редактирования
