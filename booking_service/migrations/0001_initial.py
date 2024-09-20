# Generated by Django 5.1.1 on 2024-09-19 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_in', models.DateField(verbose_name='Дата заезда')),
                ('check_out', models.DateField(verbose_name='Дата выезда')),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Итоговая цена')),
                ('status', models.CharField(choices=[('pending', 'В ожидании'), ('confirmed', 'Подтверждено'), ('cancelled', 'Отменено')], max_length=20, verbose_name='Статус бронирования')),
            ],
        ),
    ]
