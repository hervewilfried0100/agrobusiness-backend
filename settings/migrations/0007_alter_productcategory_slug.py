# Generated by Django 4.2.6 on 2023-10-22 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0006_productcategory_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcategory',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, null=True, unique=True, verbose_name='Product category slug'),
        ),
    ]