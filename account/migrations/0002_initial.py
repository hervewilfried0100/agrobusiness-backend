# Generated by Django 4.2.6 on 2023-10-12 18:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cities_light', '0011_alter_city_country_alter_city_region_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersubscription',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='subscription_user', to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
        migrations.AddField(
            model_name='subscription',
            name='offers',
            field=models.ManyToManyField(to='account.offer', verbose_name='Subscription offers'),
        ),
        migrations.AddField(
            model_name='entreprise',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entreprise_country', to='cities_light.country', verbose_name="Pays de l'entreprise"),
        ),
        migrations.AddField(
            model_name='entreprise',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entreprise_user', to=settings.AUTH_USER_MODEL, verbose_name='User entreprise'),
        ),
    ]