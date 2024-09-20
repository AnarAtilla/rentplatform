from django.db import models
from property_service.models import Property
from user_service.models import User

class Review(models.Model):
    property = models.ForeignKey(Property, related_name='reviews', on_delete=models.CASCADE, verbose_name='Недвижимость')
    guest = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Гость')
    rating = models.IntegerField(default=1, verbose_name='Рейтинг')
    comment = models.TextField(verbose_name='Комментарий', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('property', 'guest')

    def __str__(self):
        return f"{self.property.title} - {self.guest.email} ({self.rating})"
