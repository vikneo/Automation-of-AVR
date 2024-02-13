from django.dispatch import receiver
from django.db.models.signals import pre_save

from utilits.slugify import slugify



from .models import (
    TypeAVR,
    Classification,
    SmartRelay,
)


@receiver(pre_save, sender=TypeAVR)
def get_slugify_type_avr(instance, **kwargs):
    """
    
    """
    if not instance.slug:
        instance.slug = slugify(instance.name)
    
