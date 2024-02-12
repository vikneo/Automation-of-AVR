# Generated by Django 5.0.1 on 2024-02-12 03:55

import django.db.models.deletion
import imagekit.models.fields
import users.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(db_index=True, max_length=12, verbose_name='Телефон')),
                ('avatar', imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to=users.models.profile_images_directory_path, verbose_name='Фотография профиля')),
                ('archive', models.BooleanField(default=False, verbose_name='Архив')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'profile',
                'verbose_name_plural': 'profiles',
                'db_table': 'profies',
            },
        ),
    ]
