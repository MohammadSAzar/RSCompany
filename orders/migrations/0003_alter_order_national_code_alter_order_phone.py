# Generated by Django 4.2.6 on 2023-11-08 13:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_rename_price_orderitem_base_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='national_code',
            field=models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(10)], verbose_name='national_code'),
        ),
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(11), django.core.validators.MinValueValidator(11)], verbose_name='Phone Number'),
        ),
    ]
