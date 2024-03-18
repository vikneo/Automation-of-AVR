# Generated by Django 5.0.1 on 2024-03-18 02:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avr_type', '0014_classification_macro_code_alter_advantage_icon_and_more'),
        ('users', '0002_alter_profile_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('system', models.CharField(max_length=100, verbose_name='Тип АВР')),
                ('name', models.CharField(max_length=100, verbose_name='Название шкафа')),
                ('options', models.TextField(verbose_name='Опции')),
                ('status', models.IntegerField(choices=[], verbose_name='Статус заказа')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='users.profile', verbose_name='Профиль')),
            ],
            options={
                'verbose_name': 'заказ',
                'verbose_name_plural': 'заказы',
                'db_table': 'orders',
            },
        ),
    ]
