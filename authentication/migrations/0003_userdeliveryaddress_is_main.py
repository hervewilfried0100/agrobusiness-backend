# Generated by Django 4.2.6 on 2023-11-01 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_remove_userdeliveryaddress_is_main_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdeliveryaddress',
            name='is_main',
            field=models.BooleanField(default=False),
        ),
    ]
