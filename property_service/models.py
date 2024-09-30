from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator


class Property(models.Model):
    PROPERTY_TYPES = [
        ('apartment', 'Квартира'),
        ('house', 'Дом'),
        ('room', 'Комната'),
        ('studio', 'Студия'),
        ('villa', 'Вилла'),
        ('townhouse', 'Таунхаус'),
        ('bungalow', 'Бунгало'),
        ('hotel_room', 'Номер в отеле'),
        ('hostel_room', 'Номер в хостеле'),
        ('guesthouse', 'Гостевой дом'),
        ('dormitory', 'Общежитие'),
        ('cabin', 'Каюта'),
        ('cottage', 'Коттедж'),
        ('penthouse', 'Пентхаус'),
        ('loft', 'Лофт'),
        ('bed_and_breakfast', 'Пансионат/Отель типа "Bed and Breakfast"'),
        ('chalet', 'Шале'),
        ('farmhouse', 'Фермерский дом'),
        ('motel', 'Мотель'),
    ]

    title = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    location = models.CharField(max_length=255, verbose_name="Местоположение")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='properties',
                              verbose_name="Владелец")
    property_type = models.CharField(max_length=50, choices=PROPERTY_TYPES, verbose_name="Тип недвижимости")
    rooms = models.IntegerField(default=1, validators=[MinValueValidator(1)], verbose_name="Количество комнат")
    bathrooms = models.PositiveIntegerField(default=1, verbose_name="Количество ванных комнат")
    amenities = models.JSONField(null=True, blank=True, verbose_name="Удобства")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    photos = models.ImageField(upload_to='property_photos/', null=True, blank=True)

    # Поля для доступности
    available_from = models.DateField(null=True, blank=True, verbose_name="Доступно с")
    available_to = models.DateField(null=True, blank=True, verbose_name="Доступно до")

    def is_available_for_dates(self, checkin, checkout):
        """
        Проверка, доступна ли недвижимость на указанные даты по ограничениям владельца.
        """
        if self.available_from and self.available_to:
            return self.available_from <= checkin <= self.available_to and self.available_from <= checkout <= self.available_to
        return True  # Если даты доступности не заданы, считаем, что доступна всегда
    def __str__(self):
        return self.title


class PropertyImage(models.Model):
    property = models.ForeignKey(Property, related_name='images', on_delete=models.CASCADE, verbose_name="Недвижимость")
    image = models.ImageField(upload_to='property_photos/', verbose_name="Изображение")
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата загрузки")

    def __str__(self):
        return f"{self.property.title} - Image {self.id}"
