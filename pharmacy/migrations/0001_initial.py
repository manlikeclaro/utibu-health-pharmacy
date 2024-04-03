# Generated by Django 5.0.3 on 2024-04-03 16:04

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Medication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('medication_image', models.ImageField(default='pharmacy/images/default_image.png', upload_to='pharmacy/images')),
                ('description', models.TextField()),
                ('short_description', models.TextField(default='')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('stock_quantity', models.IntegerField(default=0)),
                ('slug', models.SlugField(unique=True)),
                ('sale', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'Medication',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField()),
                ('phone_number', models.CharField(max_length=15)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medication_price', models.DecimalField(decimal_places=2, default=0, editable=False, max_digits=10)),
                ('quantity', models.IntegerField(default=1)),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('total_price', models.DecimalField(decimal_places=2, default=None, editable=False, max_digits=10)),
                ('transaction_id', models.CharField(default='', editable=False, max_length=20, unique=True)),
                ('customer', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='pharmacy.customer')),
                ('medication', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pharmacy.medication')),
            ],
        ),
    ]
