# Generated by Django 4.2.6 on 2023-11-08 09:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='price',
            new_name='base_value',
        ),
    ]
