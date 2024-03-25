# Generated by Django 5.0.1 on 2024-03-25 02:44

import software.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('software', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filesoftware',
            name='file_driver',
            field=models.FileField(blank=True, null=True, upload_to=software.models.path_file_driver, verbose_name='Драйвер'),
        ),
        migrations.AlterField(
            model_name='filesoftware',
            name='file_instruction',
            field=models.FileField(blank=True, null=True, upload_to=software.models.path_file_instruction, verbose_name='Инструкция'),
        ),
    ]