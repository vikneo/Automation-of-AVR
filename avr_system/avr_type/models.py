from typing import Any
from django.db import models

from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill


def path_file_logic(instance: 'File', filename: str) -> str:
    """
    The function generates a path based on the name of the file with the algorithm.

    :param instance: object File
    :param filename: name file
    :return: str - path to save
    """
    return f"{instance.firmware.name}/logic/{filename}"


def path_file_description(instance: 'File', filename: str) -> str:
    """
    The function generates a path based on the name of the file with description the algorithm.

    :param instance: object File
    :param filename: name file
    :return: str - path to save
    """
    return f"{instance.firmware.name}/description/{filename}"


def banner_images_directory_path(instance: 'Banner', filename: str) -> str:
    """
    The function generates a path based on the name of the file with image the banner.

    :param instance: object File
    :param filename: name file
    :return: str - path to save
    """
    return f"banner/{instance.name}/{filename}"

def system_images_directory_path(instance: 'ImageTypeAVR', filename: str) -> str:
    """
    The function generates a path based on the name of the file with image for the system avr.

    :param instance: object File
    :param filename: name file
    :return: str - path to save
    """
    return f"system/{instance.type_avr}/{filename}"

def advantage_icon_directory_path(instance: 'Advantage', filename: str) -> str:
    """
    The function generates a path based on the name of the file with image the advantage.

    :param instance: object File
    :param filename: name file
    :return: str - path to save   
    """
    return f"advantage/{instance.title}/{filename}"


class TypeAVR(models.Model):
    """
    The Class description the models the types systems the AVR.
    """

    name = models.CharField(max_length=120, verbose_name='Тип АВР', db_index=True)
    slug = models.SlugField(max_length=120, verbose_name='URL')
    access = models.BooleanField(default=True, verbose_name='Доступ')

    def __str__(self) -> str:
        return f"{self.name}"
    
    class Meta:
        db_table = 'type_avr'
        verbose_name = 'system'
        verbose_name_plural = 'systems'


class ImageTypeAVR(models.Model):
    """
    
    """
    type_avr = models.ForeignKey(TypeAVR, on_delete=models.CASCADE, verbose_name='Тип системы', related_name='images')
    photo = models.ImageField(upload_to=system_images_directory_path, verbose_name='Основное фото')
    # photo = ProcessedImageField(
    #     verbose_name='Основное фото',
    #     upload_to=system_images_directory_path,
    #     options={'quantity': 60},
    #     processors=[ResizeToFill(300, 300)]
    # )
    

    def __str__(self) -> str:
        return f'{self.type_avr}'
    
    class Meta:
        db_table = 'images'
        verbose_name = 'image'
        verbose_name_plural = 'images'


class Classification(models.Model):
    """
    The Class description the models the classifications for systems the AVR.
    """
    type_avr = models.ForeignKey(TypeAVR, on_delete=models.CASCADE, verbose_name='Тип АВР', related_name='type_avrs')
    name = models.CharField(max_length=100, verbose_name='Название', db_index=True)
    slug = models.SlugField(max_length=120, verbose_name='URL')
    vnr = models.BooleanField(verbose_name='Ключ ВНР', default=False)
    temp_tp = models.BooleanField(verbose_name='Перегрев тр-ров', default=False)
    reset = models.BooleanField(verbose_name='Кнопка "Сброс"', default=False)
    shoice_in = models.BooleanField(verbose_name='Выбор ввода', default=False)
    dgu = models.BooleanField(verbose_name='Наличие ДГУ', default=False)
    work_tp = models.BooleanField(verbose_name='Режим работы тр-ров', default=False)
    status_box = models.BooleanField(verbose_name='Положение АВ в корзине', default=False)
    lamp_avr_ready = models.BooleanField(verbose_name='Лампа АВР готов', default=False)
    lamp_avr_work = models.BooleanField(verbose_name='Лампа АВР с работал', default=False)
    signal_ozz = models.BooleanField(verbose_name='Сигнал ОЗЗ', default=False)
    comment = models.TextField(verbose_name='Примечание', default='!')
    relay = models.ForeignKey("SmartRelay", on_delete=models.CASCADE, verbose_name='Тип ПЛК')
    access = models.BooleanField(default=True, verbose_name='Доступ')

    def __str__(self) -> str:
        return f'{self.name}'
    
    class Meta:
        db_table = 'classification'
        verbose_name = 'classification'
        verbose_name_plural = 'classifications'


class SmartRelay(models.Model):
    """
    The Class description the models of "types logic relay" and choices of models.
    """
    class TypeRelay(models.TextChoices):
        """
        Choices of models
        """
        PR200 = 'ПР200'
        PR205 = 'ПР205'
        PR103 = 'ПР103'
        SR3B261BD = 'SR3B261BD'
        SR2B261FU = 'SR2B261FU'
        SR2B201FU = 'SR2B201FU'
        SR2B121FU = 'SR2B121FU'
        ONI = 'Oni'
        LOGO = 'LOGO!8'

    brend = models.CharField(max_length=20, verbose_name='Бренд', db_index=True)
    model = models.CharField(max_length=20, verbose_name='Модель', choices=TypeRelay)
    slug = models.SlugField(max_length=20, verbose_name='URL')

    def __str__(self) -> Any:
        return f'{self.model}'
    
    class Meta:
        db_table = 'smart_relay'
        verbose_name = 'relay'
        verbose_name_plural = 'relays'


class File(models.Model):
    """
    The Class description the models the file for firmwares.
    """
    firmware = models.ForeignKey(
        Classification, 
        verbose_name='Адгоритм', 
        on_delete=models.CASCADE, 
        related_name='classifications'
        )
    file = models.FileField(upload_to=path_file_logic, verbose_name='Файл конфигурации', blank=True)
    file_description = models.FileField(upload_to=path_file_description, verbose_name='Описание алгоритма', blank=True)

    def get_absolute_url(self):
        return '/'
    
    class Meta:
        db_table = 'files'
        verbose_name = 'file'
        verbose_name_plural = 'files'


class Banner(models.Model):
    """
    The Class description the models the banners.
    """
    name = models.CharField(max_length=100, verbose_name='Название', db_index=True)
    slug = models.SlugField(max_length=100, verbose_name='URL', db_index=True, unique=True)
    photo = ProcessedImageField(
        verbose_name='Основное фото',
        upload_to=banner_images_directory_path,
        options={'quantity': 90},
        processors=[ResizeToFill(600, 300)]
    )
    description = models.TextField(verbose_name='Описание')
    link = models.URLField(verbose_name='Ссылка на систему')
    is_active = models.BooleanField(default=False, verbose_name='Модерация')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    def __str__(self) -> str:
        return f'{self.name}'
    
    class MEta:
        db_table = 'banners'
        ordering = ['name', ]
        verbose_name = 'banner'
        verbose_name_plural = 'banners'


class Advantage(models.Model):
    """
    
    """
    title = models.CharField(max_length=50, verbose_name='Название', db_index=True)
    icon = models.ImageField(upload_to=advantage_icon_directory_path)
    access = models.BooleanField(default=True, verbose_name='Доступ')

    def __str__(self) -> str:
        return f'{self.title}'
    
    class Meta:
        db_table = 'advantage'
        verbose_name= 'advantage'
        verbose_name_plural = 'advantages'
