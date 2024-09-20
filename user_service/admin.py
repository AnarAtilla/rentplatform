from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from user_service.models import User

# Переопределяем модель UserAdmin для кастомизации (если нужно)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_active', 'is_staff')
    search_fields = ('username', 'email')

# Регистрируем модель User с кастомным UserAdmin
admin.site.register(User, CustomUserAdmin)
