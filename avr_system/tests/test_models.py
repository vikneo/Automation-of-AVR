"""
The module for testing the models of the application
"""
from django.test import TestCase
from django.contrib.auth import get_user_model

from random import randint

from avr_type.models import (
    TypeAVR,
    Classification,
    SmartRelay,
    File
)
from users.models import Profile

NUM_FOR_TEST = 5
_RANGE = 15


class TestModelMixin(TestCase):
    """
    Mixin for testings the models
    """

    @classmethod
    def setUpTestData(cls) -> None:
        choice = SmartRelay.TypeRelay

        for index in range(NUM_FOR_TEST):
            type_avr = ''.join(chr(randint(32, 122)) for _ in range(_RANGE))

            TypeAVR.objects.create(
                name=type_avr,
                access=True if index % 3 != 0 else False,
            )

        for relay in choice:
            SmartRelay.objects.create(
                brand=relay,
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

    def test_count_created_type_avr(self):
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

    def test_brand_label(self):
        brand = SmartRelay.objects.get(id=1)
        self.assertEqual(brand._meta.get_field("brand").verbose_name, 'Бренд')

    def test_brand_field(self):
        brand = SmartRelay.objects.get(id=1)
        self.assertTrue(brand.brand)

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
            brand='brand',
            model='test_model'
        )
        relay.save()
        brand = SmartRelay.objects.get(id=10)
        self.assertEqual(relay, brand)
        self.assertEqual(relay.brand, brand.brand)
        self.assertTrue(relay.slug)

    def test_delete_one_element(self):
        SmartRelay.objects.filter(id=3).delete()
        count = SmartRelay.objects.all().count()
        self.assertEqual(count, 8)


class ClassificationTest(TestModelMixin):
    """
    Test of the "Classification" model
    """

    def setUp(self) -> None:
        for _id in range(1, NUM_FOR_TEST + 1):
            Classification.objects.create(
                type_avr=TypeAVR.objects.get(id=_id),
                name=chr(randint(32, 122)),
                relay=SmartRelay.objects.get(id=_id)
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

    def test_choice_in_label(self):
        choice_in = Classification.objects.get(id=1)
        self.assertEqual(choice_in._meta.get_field("choice_in").verbose_name, 'Выбор ввода')

    def test_dgu_label(self):
        dgu = Classification.objects.get(id=1)
        self.assertEqual(dgu._meta.get_field("dgu").verbose_name, 'Наличие ДГУ')

    def test_work_tp_label(self):
        work_tp = Classification.objects.get(id=1)
        self.assertEqual(work_tp._meta.get_field("work_tp").verbose_name, 'Режим работы тр-ров')

    def test_status_box_label(self):
        status_box = Classification.objects.get(id=1)
        self.assertEqual(status_box._meta.get_field("status_box").verbose_name, 'Положение АВ в корзине')

    def test_lamp_avr_ready_label(self):
        lamp_avr_ready = Classification.objects.get(id=1)
        self.assertEqual(lamp_avr_ready._meta.get_field("lamp_avr_ready").verbose_name, 'Лампа АВР готов')

    def test_lamp_avr_work_label(self):
        lamp_avr_work = Classification.objects.get(id=1)
        self.assertEqual(lamp_avr_work._meta.get_field("lamp_avr_work").verbose_name, 'Лампа АВР с работал')

    def test_signal_ozz_label(self):
        signal_ozz = Classification.objects.get(id=1)
        self.assertEqual(signal_ozz._meta.get_field("signal_ozz").verbose_name, 'Сигнал ОЗЗ')

    def test_comment_label(self):
        comment = Classification.objects.get(id=1)
        self.assertEqual(comment._meta.get_field("comment").verbose_name, 'Примечание')

    def test_access_label(self):
        access = Classification.objects.get(id=1)
        self.assertEqual(access._meta.get_field("access").verbose_name, 'Доступ')

    @staticmethod
    def choice_product():
        type_avr = TypeAVR.objects.get(id=3)
        relay = SmartRelay.objects.get(id=2)
        return type_avr, relay

    def test_created_product(self):
        type_avr, relay = self.choice_product()
        name = 'ВРУ'
        avr = Classification(
            type_avr=type_avr,
            name=name,
            relay=relay
        )
        avr.save()
        self.assertEqual(Classification.objects.all().count(), 6)
        self.assertEqual(name, avr.name)
        self.assertTrue(avr.slug)

    def test_update_product(self):
        type_avr, _ = self.choice_product()
        name = 'РУНН'
        avr = Classification.objects.get(type_avr=type_avr)
        avr.name = name
        avr.save()
        self.assertEqual(name, avr.name)

    def test_delete_product(self):
        count_five = Classification.objects.all().count()
        Classification.objects.filter(id=5).delete()
        self.assertFalse(Classification.objects.all().count() == count_five)


class ProfileTest(TestCase):
    """
        Test of the "Profile" model
    """

    @classmethod
    def setUpTestData(cls) -> None:
        for idx in range(NUM_FOR_TEST):
            user = get_user_model().objects.create_user(
                username=f'test_user_{idx}',
                password='test_password',
                email=f'user_{idx}@qwe.com'
            )

            Profile.objects.create(
                user=user,
                phone=''.join(str(randint(0, 9)) for _ in range(12)),
            )

    def test_user_label(self):
        user = Profile.objects.get(id=2)
        self.assertEqual(user._meta.get_field('user').verbose_name, 'Пользователь')

    def test_phone_lable(self):
        phone = Profile.objects.get(id=1)
        self.assertEqual(phone._meta.get_field('phone').verbose_name, 'Телефон')

    def test_archive_label(self):
        archive = Profile.objects.get(id=3)
        self.assertEqual(archive._meta.get_field('archive').verbose_name, 'Архив')

    def test_avatar_lable(self):
        avatar = Profile.objects.get(id=4)
        self.assertEqual(avatar._meta.get_field('avatar').verbose_name, 'Фотография профиля')

    @staticmethod
    def created_user(last_name):
        user = get_user_model().objects.create(
            username='one_user',
            password='test_password',
            last_name=last_name
        )
        profile = Profile.objects.create(
            user=user,
            phone='1234567892',
        )
        return profile

    def test_create_user(self):
        last_name = 'Murder'
        profile = self.created_user(last_name)
        self.assertEqual(last_name, profile.user.last_name)
    
    def test_get_absolute_url(self):
        profile = Profile.objects.get(id=1)
        self.assertEqual(profile.get_absolute_url(), '/account/')

    def test_update_user(self):
        last_name = 'Poncrat'
        profile = self.created_user(last_name)
        self.assertEqual(last_name, profile.user.last_name)

    def test_count_created_users(self):
        user_count = Profile.objects.all().count()
        self.assertEqual(user_count, NUM_FOR_TEST)

    def test_deleted_user(self):
        Profile.objects.filter(id=2).delete()
        self.assertFalse(Profile.objects.all().count() == NUM_FOR_TEST)
