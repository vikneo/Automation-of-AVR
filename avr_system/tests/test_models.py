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
                access = True if indx % 3 != 0 else False,
            )

    def test_name_label(self):
        name = TypeAVR.objects.get(id=1)
        self.assertEqual(name._meta.get_field('name').verbose_name, "Тип АВР")
    
    def test_slug_label(self):
        slug = TypeAVR.objects.get(id=1)
        self.assertEqual(slug._meta.get_field('slug').verbose_name, "URL")

    def test_access_label(self):
        access = TypeAVR.objects.get(id=1)
        self.assertEqual(access._meta.get_field('access').verbose_name, "Доступ")
    
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
    
    def test_created_by_slug(self):
        slug = TypeAVR.objects.get(id=3)
        self.assertTrue(slug.slug)


class SmartRelayTest(TestCase):
    """
    Test of the "SmartRelay" model
    """
    @classmethod
    def setUpTestData(cls) -> None:
        choise = SmartRelay.TypeRelay
        for relay in choise:
            SmartRelay.objects.create(
                brend=relay,
                model=relay
            )
    
    def test_brend_label(self):
        brend = SmartRelay.objects.get(id=1)
        self.assertEqual(brend._meta.get_field("brend").verbose_name, 'Бренд')

    def test_brend_field(self):
        brend = SmartRelay.objects.get(id=1)
        self.assertTrue(brend.brend)

    def test_model_label(self):
        model = SmartRelay.objects.get(id=1)
        self.assertEqual(model._meta.get_field("model").verbose_name, 'Модель')
    
    def test_model_field(self):
        model = SmartRelay.objects.get(id=1)
        self.assertTrue(model.model)

    def test_slug_label(self):
        slug = SmartRelay.objects.get(id=1)
        self.assertEqual(slug._meta.get_field("slug").verbose_name, 'URL')

    def test_slug_field(self):
        slug = SmartRelay.objects.get(id=1)
        self.assertTrue(slug.slug)

    def test_count_created_relay(self):
        count = SmartRelay.objects.all().count()
        self.assertEqual(count, 9)
        
