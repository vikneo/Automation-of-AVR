# Generated by Django 5.0.1 on 2024-03-18 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avr_type', '0015_order_scheme'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classification',
            name='access',
            field=models.BooleanField(default=False, verbose_name='Доступ'),
        ),
    ]
