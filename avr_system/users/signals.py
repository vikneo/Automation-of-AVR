from django.dispatch import receiver
from django.db.models.signals import pre_save

from .models import Profile


@receiver(pre_save, sender=Profile)
def default_avetar(sender, instance, **kwargs):
    """
    Save the default avatar for the user if no icon.
    """
    print('instance', instance)
    print('kwargs', kwargs)

