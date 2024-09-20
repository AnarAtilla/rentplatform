import random
import string
from allauth.account.adapter import DefaultAccountAdapter


class CustomUserAdapter(DefaultAccountAdapter):
    """
    Адаптер для кастомного поведения при регистрации пользователя.
    """

    def generate_unique_username(self, email):
        """
        Генерация уникального имени пользователя на основе email.
        """
        base_username = email.split('@')[0]  # Часть email до '@'
        random_suffix = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        return f"{base_username}_{random_suffix}"

    def save_user(self, request, user, form, commit=True):
        """
        Переопределение метода для сохранения пользователя.
        Если имя пользователя не введено, оно генерируется автоматически.
        """
        user = super().save_user(request, user, form, commit=False)
        username = form.cleaned_data.get('username', '').strip()

        # Если имя пользователя не введено, генерируем его
        if not username:
            username = self.generate_unique_username(user.email)
            user.username = username

        # Сохраняем пользователя
        if commit:
            user.save()
        return user
