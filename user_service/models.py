from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models

class User(AbstractUser):
    username = models.CharField(
        max_length=150,
        unique=True,
        validators=[UnicodeUsernameValidator()],
        blank=True,
        null=True,
        error_messages={
            'unique': "Пользователь с таким именем уже существует.",
        },
    )
    is_landlord = models.BooleanField(default=False, verbose_name='Является арендодателем')
    company_name = models.CharField(max_length=255, blank=True, verbose_name='Название компании')
    address = models.CharField(max_length=255, blank=True, verbose_name='Адрес')
    phone_number = models.CharField(max_length=20, blank=True, verbose_name='Телефон')
    additional_contact_info = models.TextField(blank=True, verbose_name='Доп. контакты')

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_groups',
        blank=True,
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',
        blank=True,
        verbose_name='user permissions',
    )

