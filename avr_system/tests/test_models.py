"""
The module for testing the models of the application
"""

import tempfile
from django.test import TestCase
from django.db.models.query import QuerySet
from django.contrib.auth import get_user_model
from django.db import models

from random import randint

from avr_type.models import (
    TypeAVR, 
    Classification, 
    SmartRelay,
    ImageTypeAVR,
    File, 
    Advantage, 
    Banner,
    path_file_logic,
    path_file_description,
    banner_images_directory_path,
    system_images_directory_path,
    advantage_icon_directory_path,
    )
from users.models import Profile

NUM_FOR_TEST = 5
_RANGE = 15


class ModelMixin:

    def get_select_element(self, instance: models, id: int) -> models:
        """
        The function returns an instance of the model by id number
        
        :param instance: instance the model.
        :param id: number.
        :return: instance of the model with method get
        """
        return instance.objects.get(id=id)

    def get_queryset(self, instance: models) -> QuerySet:
        """
        The function returns a set of model queries

        :param instance: instance the model.
        :return: a set of queries to the model
        """
        return instance.objects.all()


class TestModelMixin(TestCase):
    """
    Mixin for testings the models
    """

    @classmethod
    def setUpTestData(cls) -> None:
        cls.icon = tempfile.NamedTemporaryFile(suffix=".jpg").name
        cls.choice_relay = SmartRelay.TypeRelay

        for index in range(NUM_FOR_TEST):
            type_avr = cls.set_random_chars(start=32, end=122)

            TypeAVR.objects.create(
                name=type_avr,
                access=True if index % 3 != 0 else False,
            )

        for relay in cls.choice_relay:
            SmartRelay.objects.create(brand=relay, model=relay)

        for _ in range(NUM_FOR_TEST):
            Advantage.objects.create(
                title=cls.set_random_chars(start=66, end=122), icon=cls.icon
            )
        
        for index in range(NUM_FOR_TEST):
            Banner.objects.create(
                name=cls.set_random_chars(start=32, end=122),
                photo=cls.icon,
                description=f'Descriiption for elemet - {index}',
            )
    
    @staticmethod
    def set_random_chars(start: int, end: int) -> str:
        str_chars = "".join(chr(randint(start, end)) for _ in range(_RANGE))
        return str_chars


class TypeAvrTest(ModelMixin, TestModelMixin):
    """
    Test of the "TypeAVR" model
    """

    def test_name_label(self):
        name = self.get_select_element(TypeAVR, 1)
        self.assertEqual(name._meta.get_field("name").verbose_name, "Тип АВР")

    def test_slug_label(self):
        slug = self.get_select_element(TypeAVR, 1)
        self.assertEqual(slug._meta.get_field("slug").verbose_name, "URL")

    def test_access_label(self):
        access = self.get_select_element(TypeAVR, 1)
        self.assertEqual(access._meta.get_field("access").verbose_name, "Доступ")

    def test_count_created_type_avr(self):
        count = self.get_queryset(TypeAVR).count()
        self.assertEqual(count, NUM_FOR_TEST)

    def test_access_created_type_avr(self):
        access = TypeAVR.objects.filter(access=True)
        self.assertEqual(access.count(), 3)

    def test_added_access_type_avr(self):
        access = self.get_select_element(TypeAVR, 2)
        access.access = False
        access.save()
        self.assertEqual(TypeAVR.objects.filter(access=True).count(), 2)

    def test_created_by_slug(self):
        slug = self.get_select_element(TypeAVR, 3)
        self.assertTrue(slug.slug)

    def test_created_object(self):
        name = TypeAVR(name="test_type_avr")
        name.save()
        self.assertEqual(name, self.get_select_element(TypeAVR, 6))
        self.assertTrue(name.slug)
        self.assertTrue(name.access)

    def test_deleted_object(self):
        TypeAVR.objects.filter(id=3).delete()
        count = self.get_queryset(TypeAVR).count()
        self.assertEqual(count, 4)


class ImageTypeAVRTestCase(ModelMixin, TestModelMixin):
    """
    
    """
    def setUp(self) -> None:
        self.system = self.get_select_element(TypeAVR, 1)
        ImageTypeAVR.objects.create(
            type_avr=self.system,
            photo=self.icon
        )

    def test_type_avr_lable(self) -> None:
        """
        
        """
        type_avr = self.get_select_element(ImageTypeAVR, 1)
        responce = type_avr._meta.get_field('type_avr').verbose_name
        self.assertEqual(responce, 'Тип системы')
    
    def test_photo_lable(self) -> None:
        """
        
        """
        photo = self.get_select_element(ImageTypeAVR, 1)
        responce = photo._meta.get_field('photo').verbose_name
        self.assertEqual(responce, 'Основное фото')
    
    def test_count_create(self) -> None:
        """
        
        """
        quantity = self.get_queryset(ImageTypeAVR).count()
        self.assertEqual(quantity, 1)
    
    def test_create_element(self) -> None:
        ImageTypeAVR.objects.create(
            type_avr=self.system,
            photo=self.icon
        )
        self.assertEqual(self.get_queryset(ImageTypeAVR).count(), 2)
    
    def test_delete_element(self) -> None:
        self.get_select_element(ImageTypeAVR, 1).delete()
        self.assertFalse(self.get_queryset(ImageTypeAVR))

    def test_path_image_save(self) -> None:
        file_name = 'test.jpg'
        path_image = system_images_directory_path(ImageTypeAVR, file_name)
        self.assertTrue(path_image)


class SmartRelayTest(ModelMixin, TestModelMixin):
    """
    Test of the "SmartRelay" model
    """
    def test_brand_label(self):
        brand = self.get_select_element(SmartRelay, 1)
        self.assertEqual(brand._meta.get_field("brand").verbose_name, "Бренд")

    def test_brand_field(self):
        brand = self.get_select_element(SmartRelay, 1)
        self.assertTrue(brand.brand)

    def test_model_label(self):
        model = self.get_select_element(SmartRelay, 1)
        self.assertEqual(model._meta.get_field("model").verbose_name, "Модель")

    def test_model_field(self):
        model = self.get_select_element(SmartRelay, 1)
        self.assertTrue(model.model)

    def test_slug_label(self):
        slug = self.get_select_element(SmartRelay, 1)
        self.assertEqual(slug._meta.get_field("slug").verbose_name, "URL")

    def test_slug_field(self):
        slug = self.get_select_element(SmartRelay, 1)
        self.assertTrue(slug.slug)

    def test_count_created_relay(self):
        count = self.get_queryset(SmartRelay).count()
        self.assertEqual(count, 9)

    def test_created_relay(self):
        relay = SmartRelay(brand="brand", model="test_model")
        relay.save()
        brand = self.get_select_element(SmartRelay, 10)
        self.assertEqual(relay, brand)
        self.assertEqual(relay.brand, brand.brand)
        self.assertTrue(relay.slug)

    def test_delete_one_element(self):
        SmartRelay.objects.filter(id=3).delete()
        count = self.get_queryset(SmartRelay).count()
        self.assertEqual(count, 8)


class ClassificationTest(ModelMixin, TestModelMixin):
    """
    Test of the "Classification" model
    """

    def setUp(self) -> None:
        for _id in range(1, NUM_FOR_TEST + 1):
            Classification.objects.create(
                type_avr=TypeAVR.objects.get(id=_id),
                name=chr(randint(32, 122)),
                relay=SmartRelay.objects.get(id=_id),
            )

    def test_count_created_product(self):
        count_prod = self.get_queryset(Classification).count()
        self.assertEqual(count_prod, 5)

    def test_type_avr_label(self):
        type_avr = self.get_select_element(Classification, 1)
        self.assertEqual(type_avr._meta.get_field("type_avr").verbose_name, "Тип АВР")

    def test_name_label(self):
        name = self.get_select_element(Classification, 1)
        self.assertEqual(name._meta.get_field("name").verbose_name, "Название")

    def test_vnr_label(self):
        vnr = self.get_select_element(Classification, 1)
        self.assertEqual(vnr._meta.get_field("vnr").verbose_name, "Ключ ВНР")

    def test_temp_tp_label(self):
        temp_tp = self.get_select_element(Classification, 1)
        self.assertEqual(
            temp_tp._meta.get_field("temp_tp").verbose_name, "Перегрев тр-ров"
        )

    def test_reset_label(self):
        reset = self.get_select_element(Classification, 1)
        self.assertEqual(reset._meta.get_field("reset").verbose_name, 'Кнопка "Сброс"')

    def test_choice_in_label(self):
        choice_in = self.get_select_element(Classification, 1)
        self.assertEqual(
            choice_in._meta.get_field("choice_in").verbose_name, "Выбор ввода"
        )

    def test_dgu_label(self):
        dgu = self.get_select_element(Classification, 1)
        self.assertEqual(dgu._meta.get_field("dgu").verbose_name, "Наличие ДГУ")

    def test_work_tp_label(self):
        work_tp = self.get_select_element(Classification, 1)
        self.assertEqual(
            work_tp._meta.get_field("work_tp").verbose_name, "Работа тр-ров (параллель)"
        )

    def test_status_box_label(self):
        status_box = self.get_select_element(Classification, 1)
        self.assertEqual(
            status_box._meta.get_field("status_box").verbose_name,
            "Положение АВ в корзине",
        )

    def test_lamp_avr_ready_label(self):
        lamp_avr_ready = self.get_select_element(Classification, 1)
        self.assertEqual(
            lamp_avr_ready._meta.get_field("lamp_avr_ready").verbose_name,
            "Лампа АВР готов",
        )

    def test_lamp_avr_work_label(self):
        lamp_avr_work = self.get_select_element(Classification, 1)
        self.assertEqual(
            lamp_avr_work._meta.get_field("lamp_avr_work").verbose_name,
            "Лампа АВР с работал",
        )

    def test_signal_ozz_label(self):
        signal_ozz = self.get_select_element(Classification, 1)
        self.assertEqual(
            signal_ozz._meta.get_field("signal_ozz").verbose_name, "Сигнал ОЗЗ"
        )

    def test_comment_label(self):
        comment = self.get_select_element(Classification, 1)
        self.assertEqual(comment._meta.get_field("comment").verbose_name, "Примечание")

    def test_access_label(self):
        access = self.get_select_element(Classification, 1)
        self.assertEqual(access._meta.get_field("access").verbose_name, "Свободно")

    def test_created_product(self):
        type_avr = self.get_select_element(TypeAVR, 3)
        relay = self.get_select_element(SmartRelay, 2)
        name = "ВРУ"
        avr = Classification(type_avr=type_avr, name=name, relay=relay)
        avr.save()
        self.assertEqual(self.get_queryset(Classification).count(), 6)
        self.assertEqual(name, avr.name)
        self.assertTrue(avr.slug)

    def test_update_product(self):
        type_avr = self.get_select_element(TypeAVR, 3)
        name = "РУНН"
        avr = Classification.objects.get(type_avr=type_avr)
        avr.name = name
        avr.save()
        self.assertEqual(name, avr.name)

    def test_delete_product(self):
        count_five = self.get_queryset(Classification).count()
        Classification.objects.filter(id=5).delete()
        self.assertFalse(self.get_queryset(Classification).count() == count_five)


class ProfileTest(ModelMixin, TestCase):
    """
    Test of the "Profile" model
    """

    @classmethod
    def setUpTestData(cls) -> None:
        for idx in range(NUM_FOR_TEST):
            user = get_user_model().objects.create_user(
                username=f"test_user_{idx}",
                password="test_password",
                email=f"user_{idx}@qwe.com",
            )

            Profile.objects.create(
                user=user,
                phone="".join(str(randint(0, 9)) for _ in range(12)),
            )

    def test_user_label(self):
        user =self.get_select_element(Profile, id=2)
        self.assertEqual(user._meta.get_field("user").verbose_name, "Пользователь")

    def test_phone_lable(self):
        phone =self.get_select_element(Profile, id=1)
        self.assertEqual(phone._meta.get_field("phone").verbose_name, "Телефон")

    def test_archive_label(self):
        archive =self.get_select_element(Profile, id=3)
        self.assertEqual(archive._meta.get_field("archive").verbose_name, "Архив")

    def test_avatar_lable(self):
        avatar =self.get_select_element(Profile, id=4)
        self.assertEqual(
            avatar._meta.get_field("avatar").verbose_name, "Фотография профиля"
        )

    @staticmethod
    def created_user(last_name):
        user = get_user_model().objects.create(
            username="one_user", password="test_password", last_name=last_name
        )
        profile = Profile.objects.create(
            user=user,
            phone="1234567892",
        )
        return profile

    def test_create_user(self):
        last_name = "Murder"
        profile = self.created_user(last_name)
        self.assertEqual(last_name, profile.user.last_name)

    def test_get_absolute_url(self):
        profile = self.get_select_element(Profile, id=1)
        self.assertEqual(profile.get_absolute_url(), "/user/account/1/")

    def test_update_user(self):
        last_name = "Poncrat"
        profile = self.created_user(last_name)
        self.assertEqual(last_name, profile.user.last_name)

    def test_count_created_users(self):
        user_count = self.get_queryset(Profile).count()
        self.assertEqual(user_count, NUM_FOR_TEST)

    def test_deleted_user(self):
        Profile.objects.filter(id=2).delete()
        self.assertFalse(self.get_queryset(Profile).count() == NUM_FOR_TEST)


class AdvantageTestCase(ModelMixin, TestModelMixin):
    """
    Test of the "Banner" model
    """

    def test_method_str(self) -> None:
        """
        Test metod __str__
        """
        title = self.get_select_element(Advantage, 2)
        self.assertEqual(title.__str__(), title.title)

    def test_title_lable(self) -> None:
        """
        Тест текстовой метки поля "title"
        """
        title = self.get_select_element(Advantage, 1)
        responce = title._meta.get_field("title").verbose_name
        self.assertEqual(responce, "Название")

    def test_icon_lable(self) -> None:
        """
        Тест текстовой метки поля "icon"
        """
        icon = self.get_select_element(Advantage, 1)
        responce = icon._meta.get_field("icon").verbose_name
        self.assertEqual(responce, "Иконка")

    def test_access_lable(self) -> None:
        """
        Тест текстовой метки поля "access"
        """
        access = self.get_select_element(Advantage, 1)
        responce = access._meta.get_field("access").verbose_name
        self.assertEqual(responce, "Доступ")

    @staticmethod
    def quantity() -> QuerySet:
        """
        Returns the model Advantage queryset
        """
        return Advantage.objects.all()

    def test_count_created(self) -> None:
        """
        Тест на количество созданных елементов
        """
        quantity = self.get_queryset(Advantage)
        self.assertEqual(quantity.count(), NUM_FOR_TEST)

    def test_add_element(self) -> None:
        """
        test for adding an element
        """
        add = Advantage(
            title="test_titale",
        )
        add.save()
        quantity = self.get_queryset(Advantage).count()
        self.assertEqual(quantity, NUM_FOR_TEST + 1)

    def test_deleted_element(self) -> None:
        """
        Test for deleted for element
        """
        self.get_select_element(Advantage, 2).delete()
        quantity = self.get_queryset(Advantage).count()
        self.assertEqual(quantity, NUM_FOR_TEST - 1)
    
    def test_advantage_icon_path(self) -> None:
        filename = 'icon.jpg'
        file_banner = advantage_icon_directory_path(Advantage, filename)
        self.assertTrue(file_banner)


class BannerTestCase(ModelMixin, TestModelMixin):
    """ 
    Test of the "Banner" model
    """
    def test_count_create_banners(self) -> None:
        quantity = Banner.objects.all().count()
        self.assertEqual(quantity, NUM_FOR_TEST)
    
    def test_method_str(self) -> None:
        name = Banner.objects.get(id=2)
        self.assertEqual(name.__str__(), name.name)
    
    def test_name_lable(self) -> None:
        """
        Тест текстовой метки поля "name"
        """
        name = self.get_select_element(Banner, 1)
        responce = name._meta.get_field("name").verbose_name
        self.assertEqual(responce, "Название")    

    def test_slug_lable(self) -> None:
        """
        Тест текстовой метки поля "slug"
        """
        slug = self.get_select_element(Banner, 1)
        responce = slug._meta.get_field("slug").verbose_name
        self.assertEqual(responce, "URL")

    def test_photo_lable(self) -> None:
        """
        Тест текстовой метки поля "photo"
        """
        photo = self.get_select_element(Banner, 1)
        responce = photo._meta.get_field("photo").verbose_name
        self.assertEqual(responce, "Основное фото")

    def test_description_lable(self) -> None:
        """
        Тест текстовой метки поля "description"
        """
        description = self.get_select_element(Banner, 1)
        responce = description._meta.get_field("description").verbose_name
        self.assertEqual(responce, "Описание")

    def test_link_lable(self) -> None:
        """
        Тест текстовой метки поля "link"
        """
        link = self.get_select_element(Banner, 1)
        responce = link._meta.get_field("link").verbose_name
        self.assertEqual(responce, "Ссылка на систему")

    def test_is_active_lable(self) -> None:
        """
        Тест текстовой метки поля "is_active"
        """
        is_active = self.get_select_element(Banner, 1)
        responce = is_active._meta.get_field("is_active").verbose_name
        self.assertEqual(responce, "Модерация")

    def test_create_at_lable(self) -> None:
        """
        Тест текстовой метки поля "create_at"
        """
        create_at = self.get_select_element(Banner, 1)
        responce = create_at._meta.get_field("create_at").verbose_name
        self.assertEqual(responce, "Дата создания")

    def test_update_at_lable(self) -> None:
        """
        Тест текстовой метки поля "update_at"
        """
        update_at = self.get_select_element(Banner, 1)
        responce = update_at._meta.get_field("update_at").verbose_name
        self.assertEqual(responce, "Дата обновления")
    
    def test_path_file_logic(self) -> None:
        filename = 'test_file'
        file_banner = banner_images_directory_path(Banner, filename)
        self.assertTrue(file_banner)


class PathFileLogicTestCase(TestCase):
    """
    Test for generating path for saving file woth logic
    """
    def setUp(self) -> None:
        path_file = path_file_logic()