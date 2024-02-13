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


class TestModelMixin(TestCase):
    """
    
    """
    @classmethod
    def setUpTestData(cls) -> None:
        choise = SmartRelay.TypeRelay

        for indx in range(NUM_FOR_TEST):
            type_avr = ''.join(chr(randint(32, 122)) for _ in range(15))
            
            TypeAVR.objects.create(
                name=type_avr,
                access = True if indx % 3 != 0 else False,
            )
        
        for relay in choise:
            SmartRelay.objects.create(
                brend=relay,
                model=relay
            )


class TypeAvrTest(TestModelMixin):
    """
    Test of the "TypeAVR" model
    """

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
    
    def test_created_object(self):
        name = TypeAVR(
            name='test_type_avr'
        )
        name.save()
        self.assertEqual(name, TypeAVR.objects.get(id=6))
        self.assertTrue(name.slug)
        self.assertTrue(name.access)
    
    def test_deleted_object(self):
        TypeAVR.objects.filter(id=3).delete()
        count = TypeAVR.objects.all().count()
        self.assertEqual(count, 4)


class SmartRelayTest(TestModelMixin):
    """
    Test of the "SmartRelay" model
    """
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
    
    def test_created_relay(self):
        relay = SmartRelay(
            brend='brend',
            model='test_model'
        )
        relay.save()
        brend = SmartRelay.objects.get(id=10)
        self.assertEqual(relay, brend)
        self.assertEqual(relay.brend, brend.brend)
        self.assertTrue(relay.slug)
    
    def test_delete_one_element(self):
        SmartRelay.objects.filter(id=3).delete()
        count = SmartRelay.objects.all().count()
        self.assertEqual(count, 8)


class ClassificationTest(TestModelMixin):
    """
    
    """
    def setUp(self) -> None:
        for _id in range(1, NUM_FOR_TEST + 1):
            Classification.objects.create(
                type_avr=TypeAVR.objects.get(id=_id),
                name=chr(randint(32, 122)),
                relay = SmartRelay.objects.get(id=_id)
            )
    
    def test_count_created_product(self):
        count_prod = Classification.objects.all().count()
        self.assertEqual(count_prod, 5)

    def test_type_avr_label(self):
        type_avr = Classification.objects.get(id=1)
        self.assertEqual(type_avr._meta.get_field("type_avr").verbose_name, 'Тип АВР')

    def test_name_label(self):
        name = Classification.objects.get(id=1)
        self.assertEqual(name._meta.get_field("name").verbose_name, 'Название')
    
    def test_vnr_label(self):
        vnr = Classification.objects.get(id=1)
        self.assertEqual(vnr._meta.get_field("vnr").verbose_name, 'Ключ ВНР')

    def test_temp_tp_label(self):
        temp_tp = Classification.objects.get(id=1)
        self.assertEqual(temp_tp._meta.get_field("temp_tp").verbose_name, 'Перегрев тр-ров')

    def test_reset_label(self):
        reset = Classification.objects.get(id=1)
        self.assertEqual(reset._meta.get_field("reset").verbose_name, 'Кнопка "Сброс"')
    def test_shoice_in_label(self):
        shoice_in = Classification.objects.get(id=1)
        self.assertEqual(shoice_in._meta.get_field("shoice_in").verbose_name, 'Выбор ввода')

    def test_dgu_label(self):
        dgu = Classification.objects.get(id=1)
        self.assertEqual(dgu._meta.get_field("dgu").verbose_name, 'Наличие ДГУ')

    def test_work_tp_label(self):
        work_tp = Classification.objects.get(id=1)
        self.assertEqual(work_tp._meta.get_field("work_tp").verbose_name, 'Режим работы тр-ров')
    
    def test_status_box_label(self):
        status_box = Classification.objects.get(id=1)
        self.assertEqual(status_box._meta.get_field("status_box").verbose_name, 'Положение АВ в корзине')

    #=========================================