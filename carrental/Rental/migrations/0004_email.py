# Generated by Django 4.2.4 on 2023-09-02 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Rental', '0003_alter_car_deposit_alter_car_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
            ],
        ),
    ]
