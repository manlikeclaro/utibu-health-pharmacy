# Generated by Django 5.0.3 on 2024-03-30 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharmacy', '0006_alter_medication_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='medication',
            name='short_description',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='medication',
            name='slug',
            field=models.SlugField(default='', unique=True),
        ),
    ]
