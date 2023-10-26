# Generated by Django 4.2.6 on 2023-10-26 01:24

import core.validators
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cities_light', '0011_alter_city_country_alter_city_region_and_more'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='uploads/user_images', validators=[core.validators.validate_image_size, core.validators.validate_image_extension], verbose_name='Photo de profil')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('is_verified', models.BooleanField(default=False, verbose_name='Est vérifié ?')),
                ('profil_type', models.CharField(choices=[('USER', 'Utilisateur'), ('AGRIPRENEUR', 'Agripreneur'), ('MERCHANT', 'Commerçant')], default='USER', max_length=255, verbose_name='Profil type')),
                ('phone_number', models.CharField(blank=True, max_length=255, null=True)),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cities_light.country')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='BroadcastGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('type_user', models.CharField(choices=[('USER', 'Utilisateur'), ('AGRIPRENEUR', 'Agripreneur'), ('MERCHANT', 'Commerçant')], default='USER', max_length=255, verbose_name='Profil type')),
                ('is_entreprise', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='HOTPDevice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(blank=True, help_text='A hex-encoded secret key of up to 40 bytes.', max_length=80, validators=[django.core.validators.MinLengthValidator(40)])),
                ('counter', models.BigIntegerField(blank=True, default=0, help_text='The counter value of the latest verified token. The next token must be at a higher counter value.')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='hotp', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
