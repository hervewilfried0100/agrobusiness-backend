# Generated by Django 4.2.6 on 2023-11-14 09:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cities_light', '0011_alter_city_country_alter_city_region_and_more'),
        ('advert', '0014_alter_product_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='made_in',
            field=models.ForeignKey(blank=True, max_length=255, null=True, on_delete=django.db.models.deletion.CASCADE, to='cities_light.country', verbose_name='Product made in'),
        ),
    ]