# Generated by Django 4.2.6 on 2023-11-01 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0004_alter_case_datetime_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='datetime_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
