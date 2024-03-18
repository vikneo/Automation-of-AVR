# Generated by Django 5.0.1 on 2024-03-18 07:51

import avr_type.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avr_type', '0013_rename_shoice_in_classification_choice_in_and_more'),
        ('users', '0002_alter_profile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='classification',
            name='macro_code',
            field=models.CharField(default=1, max_length=12, verbose_name='Код к макросам'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='advantage',
            name='icon',
            field=models.ImageField(upload_to=avr_type.models.advantage_icon_directory_path, verbose_name='Иконка'),
        ),
        migrations.AlterField(
            model_name='classification',
            name='work_tp',
            field=models.BooleanField(default=True, verbose_name='Режим работы тр-ров'),
        ),
        migrations.AlterField(
            model_name='file',
            name='firmware',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='classifications', to='avr_type.classification', verbose_name='Алгоритм'),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('system', models.CharField(max_length=100, verbose_name='Тип АВР')),
                ('name', models.CharField(max_length=100, verbose_name='Название шкафа')),
                ('options', models.TextField(verbose_name='Опции')),
                ('status', models.CharField(choices=[(None, 'Статус заказа'), ('В обработке', 'Process'), ('Заказано', 'Ordered'), ('Готов', 'Ready'), ('В работе', 'Work')], max_length=15, verbose_name='Статус заказа')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('access', models.BooleanField(default=False, verbose_name='Архив')),
                ('description', models.FileField(upload_to=avr_type.models.path_order_file_description, verbose_name='Описание алгоритма')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='users.profile', verbose_name='Профиль')),
            ],
            options={
                'verbose_name': 'заказ',
                'verbose_name_plural': 'заказы',
                'db_table': 'orders',
            },
        ),
    ]
