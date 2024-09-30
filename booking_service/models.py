from dirtyfields import DirtyFieldsMixin
from django.db import models
from django.conf import settings
from datetime import date
from property_service.models import Property

class Booking(DirtyFieldsMixin, models.Model):
    STATUS_CHOICES = [
        ('pending', 'Ожидает подтверждения'),
        ('confirmed', 'Подтверждено'),
        ('cancelled', 'Отменено'),
        ('completed', 'Завершено'),
    ]

    rental_property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='bookings',
                                        verbose_name='Недвижимость')
    guest = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='bookings',
                              verbose_name='Гость')
    check_in = models.DateField(verbose_name='Дата заезда')
    check_out = models.DateField(verbose_name='Дата выезда')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Общая стоимость', null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending',
                              verbose_name='Статус бронирования')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    def __str__(self):
        return f'Бронирование {self.rental_property.title} для {self.guest.email}'

    @property
    def is_confirmed(self):
        """Проверяет, подтверждено ли бронирование"""
        return self.status == 'confirmed'

    @property
    def is_completed(self):
        """Проверяет, завершено ли бронирование (если check_out дата прошла)"""
        return self.check_out < date.today()

    def calculate_total_price(self):
        """
        Метод для расчёта общей стоимости бронирования.
        """
        if self.check_in and self.check_out:
            days = (self.check_out - self.check_in).days
            if days < 0:
                raise ValueError('Дата выезда не может быть раньше даты заезда.')
            # Если у объекта недвижимости есть цена
            if self.rental_property and self.rental_property.price:
                return max(0, days * self.rental_property.price)  # Цена не может быть отрицательной
        return 0

    def has_conflicting_booking(self):
        """
        Проверяет, есть ли пересекающиеся бронирования на те же даты для этой недвижимости.
        """
        # Проверяем только подтвержденные бронирования
        conflicting_bookings = Booking.objects.filter(
            rental_property=self.rental_property,
            status='confirmed',
            check_in__lt=self.check_out,  # Начало существующего бронирования до конца текущего
            check_out__gt=self.check_in   # Конец существующего бронирования после начала текущего
        ).exclude(id=self.id)  # Исключаем текущее бронирование, если оно уже существует

        return conflicting_bookings.exists()

    def save(self, *args, **kwargs):
        """
        Переопределение метода save для автоматического расчета цены и отслеживания изменений статуса.
        """
        if not self.total_price:  # Рассчитываем общую стоимость, если она не указана
            self.total_price = self.calculate_total_price()

        # Проверка изменения статуса
        if 'status' in self.get_dirty_fields():
            # Добавьте здесь логику, которая срабатывает при изменении статуса
            print(f"Статус изменен на: {self.status}")

        super().save(*args, **kwargs)
