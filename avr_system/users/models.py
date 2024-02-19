from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse_lazy

from imagekit.models import ProcessedImageField
from pilkit.processors import ResizeToFit


def profile_images_directory_path(instance: "Profile", filename: str) -> str:
    """
    The function generates a path for saving images linked to the user name.

    :param instance: object Profile.
    :param filename: name file image.
    :return: str - path for save.
    """
    return f'profiles/{instance.user}/avatar/{filename}'


class Profile(models.Model):
    """
    The class describes the user's profile.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    phone = models.CharField(max_length=12, verbose_name='Телефон', db_index=True)
    avatar = ProcessedImageField(
        blank=True,
        verbose_name='Фотография профиля',
        upload_to=profile_images_directory_path,
        options={"quality": 80},
        processors=[ResizeToFit(200, 200, mat_color='white')],
        null=True

    )
    archive = models.BooleanField(default=False, verbose_name='Архив')

    def __str__(self) -> str:
        return self.user.username
    
    def get_absolute_url(self):
        return reverse_lazy('users:account')
    
    class Meta:
        db_table = 'profies'
        verbose_name = 'profile'
        verbose_name_plural = 'profiles'
