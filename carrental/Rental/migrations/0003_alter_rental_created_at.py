# Generated by Django 4.2.4 on 2023-08-26 10:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Rental', '0002_remove_userprofile_address_remove_userprofile_phone_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rental',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
