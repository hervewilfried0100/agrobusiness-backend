# Generated by Django 4.2.6 on 2023-11-01 12:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_remove_store_country'),
        ('advert', '0008_alter_product_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='entreprise',
        ),
        migrations.AddField(
            model_name='product',
            name='store',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_seller_store', to='account.store', verbose_name='Product seller store'),
        ),
    ]
