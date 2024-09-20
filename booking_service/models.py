from django.db import models
from property_service.models import Property
from user_service.models import User

class Booking(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='bookings', verbose_name='Недвижимость')
    guest = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings', verbose_name='Гость')
    check_in = models.DateField(verbose_name='Дата заезда')
    check_out = models.DateField(verbose_name='Дата выезда')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Итоговая цена')
    status = models.CharField(
        max_length=20,
        choices=[('pending', 'В ожидании'), ('confirmed', 'Подтверждено'), ('cancelled', 'Отменено')],
        verbose_name='Статус бронирования'
    )

    def __str__(self):
        return f"Бронирование {self.property.title} для {self.guest.email}"
