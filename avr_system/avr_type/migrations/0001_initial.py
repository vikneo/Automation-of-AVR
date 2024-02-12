# Generated by Django 5.0.1 on 2024-02-07 08:54

import avr_type.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, verbose_name='Название')),
                ('vnr', models.BooleanField(default=False, verbose_name='Ключ ВНР')),
                ('temp_tp', models.BooleanField(default=False, verbose_name='Перегрев тр-ров')),
                ('reset', models.BooleanField(default=False, verbose_name='Кнопка "Сброс"')),
                ('shoice_in', models.BooleanField(default=False, verbose_name='Выбор ввода')),
                ('dgu', models.BooleanField(default=False, verbose_name='Наличие ДГУ')),
                ('work_tp', models.BooleanField(default=False, verbose_name='Режим работы тр-ров')),
                ('status_box', models.BooleanField(default=False, verbose_name='Положение АВ в корзине')),
                ('lamp_avr_ready', models.BooleanField(default=False, verbose_name='Лампа АВР готов')),
                ('lamp_avr_work', models.BooleanField(default=False, verbose_name='Лампа АВР с работал')),
                ('signal_ozz', models.BooleanField(default=False, verbose_name='Сигнал ОЗЗ')),
                ('comment', models.TextField(default='!', verbose_name='Примечание')),
            ],
            options={
                'verbose_name': 'classification',
                'verbose_name_plural': 'classifications',
                'db_table': 'classification',
            },
        ),
        migrations.CreateModel(
            name='SmartRelay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brend', models.CharField(db_index=True, max_length=20, verbose_name='Бренд')),
                ('model', models.IntegerField(choices=[(1, 'ПР200'), (2, 'ПР205'), (3, 'ПР103'), (4, 'SR3B261BD'), (5, 'SR2B261FU'), (6, 'SR2B201FU'), (7, 'SR2B121FU'), (8, 'Oni'), (9, 'LOGO!8')], verbose_name='Модель')),
                ('slug', models.SlugField(max_length=20, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'relay',
                'verbose_name_plural': 'relays',
                'db_table': 'smart_relay',
            },
        ),
        migrations.CreateModel(
            name='TypeAVR',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=120, verbose_name='Тип АВР')),
                ('slug', models.SlugField(max_length=120, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'system',
                'verbose_name_plural': 'systems',
                'db_table': 'type_avr',
            },
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, upload_to=avr_type.models.path_file_logic, verbose_name='Файл конфигурации')),
                ('file_description', models.FileField(blank=True, upload_to=avr_type.models.path_file_description, verbose_name='Описание алгоритма')),
                ('firmware', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='classifications', to='avr_type.classification', verbose_name='Адгоритм')),
            ],
            options={
                'verbose_name': 'file',
                'verbose_name_plural': 'files',
                'db_table': 'files',
            },
        ),
        migrations.AddField(
            model_name='classification',
            name='relay',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='avr_type.smartrelay', verbose_name='Тип ПЛК'),
        ),
        migrations.AddField(
            model_name='classification',
            name='type_avr',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='type_avrs', to='avr_type.typeavr', verbose_name='Тип АВР'),
        ),
    ]