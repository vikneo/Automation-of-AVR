# Generated by Django 5.0.1 on 2024-02-16 08:33

import avr_type.models
import django.db.models.deletion
import imagekit.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avr_type', '0007_banner_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageTypeAVR',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', imagekit.models.fields.ProcessedImageField(upload_to=avr_type.models.banner_images_directory_path, verbose_name='Основное фото')),
                ('type_avr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='avr_type.typeavr', verbose_name='Тип системы')),
            ],
            options={
                'verbose_name': 'image',
                'verbose_name_plural': 'images',
                'db_table': 'images',
            },
        ),
    ]
