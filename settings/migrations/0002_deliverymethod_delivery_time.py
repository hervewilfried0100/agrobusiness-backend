# Generated by Django 4.2.6 on 2023-10-19 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='deliverymethod',
            name='delivery_time',
            field=models.PositiveSmallIntegerField(default=1, verbose_name='Delivery method delivery time in days'),
        ),
    ]
