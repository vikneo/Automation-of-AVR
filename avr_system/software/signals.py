from django.dispatch import receiver
from django.db.models.signals import pre_save

from utilits.slugify import slugify
from .models import SoftWare


@receiver(pre_save, sender=SoftWare)
def get_slugify_sogtware(instance, **kwargs) -> None:
    """
    Before saving the model, the "slug" field is checked, 
    if the field is empty, it is filled in from the "name" 
    field through the "slugify" module
    """
    if not instance.slug:
        instance.slug = slugify(instance.name)
