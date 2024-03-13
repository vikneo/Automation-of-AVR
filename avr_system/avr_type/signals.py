from django.dispatch import receiver
from django.db.models.signals import pre_save

from utilits.slugify import slugify

from .models import (
    TypeAVR,
    Classification,
    SmartRelay,
    Banner,
)


@receiver(pre_save, sender=Banner)
@receiver(pre_save, sender=Classification)
@receiver(pre_save, sender=TypeAVR)
def get_slugify_type_avr(instance, **kwargs) -> None:
    """
    Before saving the model, the "slug" field is checked, 
    if the field is empty, it is filled in from the "name" 
    field through the "slugify" module
    """
    if not instance.slug:
        instance.slug = slugify(instance.name)


@receiver(pre_save, sender=SmartRelay)
def get_slugify_smart_relay(instance, **kwargs) -> None:
    """
    Before saving the model, the "slug" field is checked, 
    if the field is empty, it is filled in from the "model" 
    field through the "slugify" module
    """
    if not instance.slug:
        instance.slug = slugify(instance.model)
