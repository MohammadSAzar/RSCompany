# Generated by Django 4.2.6 on 2023-10-27 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0002_alter_case_end_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='cover',
            field=models.ImageField(blank=True, upload_to='cases/', verbose_name='cover'),
        ),
    ]