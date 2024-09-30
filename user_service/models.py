from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    username = None  # Убираем username, используем email
    email = models.EmailField(unique=True, verbose_name="Email", error_messages={
        'unique': "Пользователь с таким email уже существует.",
    })

    # Дополнительные поля для пользователя
    is_landlord = models.BooleanField(default=False, verbose_name='Является арендодателем')
    is_business_account = models.BooleanField(default=False, verbose_name='Бизнес-аккаунт')
    company_name = models.CharField(max_length=255, blank=True, verbose_name='Название компании')
    address = models.CharField(max_length=255, blank=True, verbose_name='Адрес')
    phone_number = models.CharField(max_length=20, blank=True, verbose_name='Телефон')
    additional_contact_info = models.TextField(blank=True, verbose_name='Дополнительная контактная информация')

    # Статусы пользователя
    STATUS_CHOICES = [
        ('pending', 'Ожидание активации'),
        ('active', 'Активен'),
        ('deactivated', 'Деактивирован'),
        ('deleted', 'Удален'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending', verbose_name='Статус')
    status_changed_at = models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения статуса')

    # Связь Many-to-Many с группами и правами (уникальные related_name)
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_groups',  # Измененный related_name для избежания конфликтов
        blank=True,
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',  # Измененный related_name
        blank=True,
        verbose_name='user permissions',
    )

    # Используем email как основной идентификатор
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


