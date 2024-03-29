# Generated by Django 5.0.1 on 2024-02-19 03:19

import avr_type.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avr_type', '0010_alter_imagetypeavr_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advantage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=50, verbose_name='Название')),
                ('icon', models.ImageField(upload_to=avr_type.models.advantage_icon_directory_path)),
            ],
            options={
                'verbose_name': 'advantage',
                'verbose_name_plural': 'advantages',
                'db_table': 'advantage',
            },
        ),
    ]
