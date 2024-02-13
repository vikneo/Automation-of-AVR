from django.dispatch import receiver
from django.db.models.signals import pre_save

from utilits.slugify import slugify



from .models import (
    TypeAVR,
    Classification,
    SmartRelay,
)

@receiver(pre_save, sender=Classification)
@receiver(pre_save, sender=TypeAVR)
def get_slugify_type_avr(instance, **kwargs) -> None:
    """
    
    """
    if not instance.slug:
        instance.slug = slugify(instance.name)
    
@receiver(pre_save, sender=SmartRelay)
def get_slugify_smart_relay(instance, **kwargs) -> None:
    """
    
    """
    if not instance.slug:
        instance.slug = slugify(instance.model)
