from django.dispatch import receiver
from django.db.models.signals import pre_save
from django.contrib.auth.models import User

from .models import Profile


@receiver(pre_save, sender=Profile)
def default_avatar(sender, instance, **kwargs):
    """
    Save the default avatar for the user if no icon.
    """
    if not instance.avatar:
        instance.avatar = 'default/avatar/avatar.jpg'

    if instance.archive:
        instance.user.is_active = False
    else:
        instance.user.is_active = True

    instance.user.save()


@receiver(pre_save, sender=User)
def create_username(sender, instance, **kwargs):
    """
    Create the username for the User if no username
    """
    if not instance.username:
        instance.username = f"NotUserName{instance.id}"
        instance.save()
