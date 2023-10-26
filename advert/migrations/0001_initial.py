# Generated by Django 4.2.6 on 2023-10-26 01:01

import ckeditor.fields
import core.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('settings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Product name')),
                ('short_description', models.TextField(blank=True, null=True, verbose_name='Product short description')),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Product description')),
                ('price', models.FloatField(verbose_name='Product price')),
                ('quantity', models.PositiveIntegerField(default=0, verbose_name='Product quantity')),
                ('status', models.CharField(choices=[('PUBLISH', 'Publié'), ('UNPUBLISH', 'Non publié'), ('WAIT', 'En attente'), ('REFUSED', 'Refusé')], default='UNPUBLISH', max_length=255, verbose_name='Product status')),
                ('stock_status', models.CharField(choices=[('IN_STOCK', 'En stock'), ('OUT_OF_STOCK', 'En rupture de stock')], default='IN_STOCK', max_length=255, verbose_name='Product stock status')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Product created at')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.CreateModel(
            name='ProductCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Product cart created at')),
            ],
        ),
        migrations.CreateModel(
            name='ProductComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(verbose_name='Product comment')),
                ('rating', models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)], verbose_name='Product comment rating')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Product comment created at')),
            ],
            options={
                'verbose_name': 'Product comment',
                'verbose_name_plural': 'Product comments',
            },
        ),
        migrations.CreateModel(
            name='ProductFavorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Product favorite created at')),
            ],
            options={
                'verbose_name': 'Product favorite',
                'verbose_name_plural': 'Product favorites',
            },
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_main', models.BooleanField(default=False, verbose_name='Is main product image')),
                ('image', models.ImageField(upload_to='uploads/product_images', validators=[core.validators.validate_image_size, core.validators.validate_image_extension], verbose_name='Product image')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Product image created at')),
            ],
            options={
                'verbose_name': 'Product image',
                'verbose_name_plural': 'Product images',
            },
        ),
        migrations.CreateModel(
            name='ProductOrder',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('reference', models.CharField(max_length=255, unique=True, verbose_name='Product order reference')),
                ('total_price', models.FloatField(verbose_name='Product order price')),
                ('status', models.CharField(choices=[('PENDING', 'En attente'), ('RECEIVED', 'Reçu'), ('DELIVERED', 'Livré'), ('CANCELED', 'Annulé')], default='PENDING', max_length=255, verbose_name='Product order status')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Product order created at')),
            ],
            options={
                'verbose_name': 'Product order',
                'verbose_name_plural': 'Product orders',
            },
        ),
        migrations.CreateModel(
            name='ProductOrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(verbose_name='Product order item quantity')),
                ('unit_price', models.FloatField(verbose_name='Product order item unit price')),
                ('total_price', models.FloatField(verbose_name='Product order item total price')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Product order item created at')),
            ],
            options={
                'verbose_name': 'Product order item',
                'verbose_name_plural': 'Product order items',
            },
        ),
        migrations.CreateModel(
            name='ProductsSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nom de la section')),
                ('description', models.TextField(verbose_name='Description de la section')),
                ('product_type', models.CharField(choices=[('ALL_PRODUCTS', 'Tous les produits'), ('NEW_ADDED_PRODUCTS', 'Nouveaux produits ajoutés')], default='ALL_PRODUCTS', max_length=255, verbose_name='Product type')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Section created at')),
            ],
        ),
        migrations.CreateModel(
            name='SellerDelivery',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('delivery_time', models.PositiveIntegerField(verbose_name='Seller delivery delivery time in days')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Seller delivery created at')),
                ('delivery_method', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seller_delivery_method', to='settings.deliverymethod', verbose_name='Seller delivery delivery method')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seller_delivery_product', to='advert.product', verbose_name='Seller delivery product')),
            ],
            options={
                'verbose_name': 'Seller delivery',
                'verbose_name_plural': 'Seller deliveries',
            },
        ),
    ]
