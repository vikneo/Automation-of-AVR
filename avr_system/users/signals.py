from django.dispatch import receiver
from django.db.models.signals import pre_save

from .models import Profile


@receiver(pre_save, sender=Profile)
def default_avatar(sender, instance, **kwargs):
    """
    Save the default avatar for the user if no icon.
    """
    if not instance.avatar:
        instance.avatar = 'default/avatar/avatar.jpg'

