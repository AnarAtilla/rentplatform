# Generated by Django 5.1.1 on 2024-09-20 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property_service', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='amenities',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='bathrooms',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='property',
            name='photos',
            field=models.ImageField(blank=True, null=True, upload_to='property_photos/'),
        ),
        migrations.AddField(
            model_name='property',
            name='property_type',
            field=models.CharField(choices=[('apartment', 'Квартира'), ('house', 'Дом'), ('room', 'Комната')], default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='property',
            name='rooms',
            field=models.IntegerField(default=1),
        ),
    ]
