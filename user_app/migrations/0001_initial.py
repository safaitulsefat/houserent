# Generated by Django 4.1.7 on 2023-05-11 15:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='OwnerRent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('property_type', models.CharField(blank=True, max_length=255, null=True)),
                ('rent_type', models.CharField(blank=True, max_length=255, null=True)),
                ('division', models.CharField(blank=True, max_length=20, null=True)),
                ('district', models.CharField(blank=True, max_length=20, null=True)),
                ('property_location', models.TextField(blank=True, max_length=100, null=True)),
                ('rent_money', models.IntegerField(blank=True, null=True)),
                ('money_type', models.CharField(blank=True, max_length=255, null=True)),
                ('floor_no', models.CharField(blank=True, max_length=20, null=True)),
                ('floor_face', models.CharField(blank=True, max_length=50, null=True)),
                ('plot_size', models.IntegerField(blank=True, null=True)),
                ('numerical_value_type', models.TextField(blank=True, max_length=50, null=True)),
                ('area_description', models.TextField(blank=True, max_length=250, null=True)),
                ('rent_photo', models.ImageField(blank=True, null=True, upload_to='rent')),
                ('date_added', models.DateTimeField(auto_now_add=True, null=True)),
                ('user_email', models.EmailField(blank=True, max_length=200, null=True)),
                ('phone_no', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sell_land',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('divission', models.CharField(blank=True, max_length=20, null=True)),
                ('district', models.CharField(blank=True, max_length=20, null=True)),
                ('location', models.TextField(blank=True, max_length=255, null=True)),
                ('price', models.BigIntegerField(blank=True, null=True)),
                ('ammount', models.CharField(blank=True, max_length=50, null=True)),
                ('plots_count', models.IntegerField(blank=True, null=True)),
                ('land_type', models.CharField(blank=True, max_length=50, null=True)),
                ('details', models.TextField(blank=True, null=True)),
                ('land_image', models.ImageField(blank=True, null=True, upload_to='land_photos')),
                ('date_added', models.DateTimeField(auto_now_add=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Sell_flat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('divission', models.CharField(blank=True, max_length=20, null=True)),
                ('district', models.CharField(blank=True, max_length=20, null=True)),
                ('location', models.TextField(blank=True, max_length=255, null=True)),
                ('price', models.BigIntegerField(blank=True, null=True)),
                ('ammount', models.CharField(blank=True, max_length=50, null=True)),
                ('floors_count', models.IntegerField(blank=True, null=True)),
                ('floor_face', models.CharField(blank=True, max_length=50, null=True)),
                ('details', models.TextField(blank=True, null=True)),
                ('flat_image', models.ImageField(blank=True, null=True, upload_to='flat_photos')),
                ('date_added', models.DateTimeField(auto_now_add=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
