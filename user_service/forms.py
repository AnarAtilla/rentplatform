from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm as AuthPasswordChangeForm

class UserProfileForm(UserChangeForm):
    """
    Форма для редактирования профиля пользователя
    """
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

class PasswordChangeForm(AuthPasswordChangeForm):
    """
    Форма для изменения пароля
    """
    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']
