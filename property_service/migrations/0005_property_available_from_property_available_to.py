# Generated by Django 5.1.1 on 2024-09-28 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property_service', '0004_property_photos_alter_property_rooms'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='available_from',
            field=models.DateField(blank=True, null=True, verbose_name='Доступно с'),
        ),
        migrations.AddField(
            model_name='property',
            name='available_to',
            field=models.DateField(blank=True, null=True, verbose_name='Доступно до'),
        ),
    ]
