from django.db import models
from django.conf import settings

class Notification(models.Model):
    RECIPIENT_TYPES = [
        ('user', 'Пользователь'),
        ('admin', 'Администратор'),
    ]

    recipient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='notifications', verbose_name='Получатель')
    recipient_type = models.CharField(max_length=10, choices=RECIPIENT_TYPES, default='user', verbose_name='Тип получателя')
    message = models.TextField(verbose_name='Сообщение')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    read = models.BooleanField(default=False, verbose_name='Прочитано')

    def __str__(self):
        return f'Уведомление для {self.recipient.email}'