# Generated by Django 4.2.6 on 2023-10-19 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advert', '0006_remove_productorder_delivery_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=models.ImageField(upload_to='uploads/product_images', verbose_name='Product image'),
        ),
    ]
