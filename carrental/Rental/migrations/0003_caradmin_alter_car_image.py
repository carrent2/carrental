# Generated by Django 4.2.4 on 2023-08-27 10:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Rental', '0002_remove_userprofile_address_remove_userprofile_phone_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarAdmin',
            fields=[
                ('car_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Rental.car')),
            ],
            options={
                'abstract': False,
            },
            bases=('Rental.car',),
        ),
        migrations.AlterField(
            model_name='car',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/%Y/%m/%d'),
        ),
    ]