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
    print('Зашли в метод pre_save')
    if not instance.slug:
        print('Поле slug - пустое')
        instance.slug = slugify(instance.name)
    print('Поле slug - не пустое')
    
