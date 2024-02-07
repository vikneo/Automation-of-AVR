from typing import Any
from django.db import models


def path_file_logic(instance: 'File', filename: str) -> str:
    """
    The function generates a path based on the name of the file with the algorithm.

    :param instance: object File
    :param filename: name file
    :return: str - path to save
    """
    return f"{isinstance.firmware.name}/logic/{filename}"


def path_file_description(instance: 'File', filename: str) -> str:
    """
    The function generates a path based on the name of the file with description the algorithm.

    :param instance: object File
    :param filename: name file
    :return: str - path to save
    """
    return f"{isinstance.firmware.name}/description/{filename}"


class TypeAVR(models.Model):
    """
    The Class description the models the types systems the AVR.
    """

    name = models.CharField(max_length=120, verbose_name='Тип АВР', db_index=True)
    slug = models.SlugField(max_length=120, verbose_name='URL')

    def __str__(self) -> str:
        return f"{self.name}"
    
    class Meta:
        db_table = 'type_avr'
        verbose_name = 'system'
        verbose_name_plural = 'systems'


class Classification(models.Model):
    """
    The Class description the models the classifications for systems the AVR.
    """
    type_avr = models.ForeignKey(TypeAVR, on_delete=models.CASCADE, verbose_name='Тип АВР', related_name='type_avrs')
    name = models.CharField(max_length=100, verbose_name='Название', db_index=True)
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
    class TypeRelay(models.IntegerChoices):
        """
        Choices of models
        """
        PR200 = 1, 'ПР200'
        PR205 = 2, 'ПР205'
        PR103 = 3, 'ПР103'
        SR3B261BD = 4, 'SR3B261BD'
        SR2B261FU = 5, 'SR2B261FU'
        SR2B201FU = 6, 'SR2B201FU'
        SR2B121FU = 7, 'SR2B121FU'
        ONI = 8, 'Oni'
        LOGO = 9, 'LOGO!8'

    brend = models.CharField(max_length=20, verbose_name='Бренд', db_index=True)
    model = models.IntegerField(verbose_name='Модель', choices=TypeRelay.choices)
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
