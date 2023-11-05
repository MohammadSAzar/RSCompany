# Generated by Django 4.2.6 on 2023-11-05 14:06

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0005_alter_case_datetime_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='meter',
            field=models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(100)], verbose_name='meter'),
        ),
    ]
