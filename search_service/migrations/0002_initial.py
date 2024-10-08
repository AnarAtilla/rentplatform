# Generated by Django 5.1.1 on 2024-09-26 00:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('property_service', '0001_initial'),
        ('search_service', '0001_initial'),
        ('user_service', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='propertyviewanalytics',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='search_property_views', to='user_service.user'),
        ),
        migrations.AddField(
            model_name='searchanalytics',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='search_search_analytics', to='user_service.user'),
        ),
        migrations.AddField(
            model_name='searchhistory',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='search_search_history', to='user_service.user'),
        ),
        migrations.AddField(
            model_name='viewhistory',
            name='property',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='search_viewed_properties', to='property_service.property'),
        ),
        migrations.AddField(
            model_name='viewhistory',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='search_view_history', to='user_service.user'),
        ),
    ]
