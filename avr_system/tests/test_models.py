"""
The module for testing the models of the application
"""
from django.test import TestCase
from utilits.slugify import slugify

from random import randint

from avr_type.models import (
    TypeAVR,
    Classification,
    SmartRelay,
    File
    )
from users.models import Profile

NUM_FOR_TEST = 5


class TypeAvrTest(TestCase):
    """
    Test of the "TypeAVR" model
    """

    @classmethod
    def setUpTestData(cls) -> None:
        for indx in range(NUM_FOR_TEST):
            type_avr = ''.join(chr(randint(32, 122)) for _ in range(15))
            
            TypeAVR.objects.create(
                name=type_avr,
                # slug = slugify(type_avr),
                access = True if indx % 3 != 0 else False,
            )

    def test_name_label(self):
        name = TypeAVR.objects.get(id=1)
        self.assertEqual(name._meta.get_field('name').verbose_name, "Тип АВР")
    
    def test_slug_label(self):
        name = TypeAVR.objects.get(id=1)
        self.assertEqual(name._meta.get_field('slug').verbose_name, "URL")

    def test_access_label(self):
        name = TypeAVR.objects.get(id=1)
        self.assertEqual(name._meta.get_field('access').verbose_name, "Доступ")
    
    def  test_count_created_type_avr(self):
        count = TypeAVR.objects.all().count()
        self.assertEqual(count, NUM_FOR_TEST)
    
    def test_access_created_type_avr(self):
        access = TypeAVR.objects.filter(access=True)
        self.assertEqual(access.count(), 3)

    def test_added_access_type_avr(self):
        access = TypeAVR.objects.get(id=2)
        access.access = False
        access.save()
        self.assertEqual(TypeAVR.objects.filter(access=True).count(), 2)
