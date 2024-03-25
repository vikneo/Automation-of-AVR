from django.db import models


def path_file_service(instance: 'FileSoftware', filename: str) -> str:
    """
    The function generates a path based on the name of the file with the algorithm.

    :param instance: object File
    :param filename: name file
    :return: str - path to save
    """
    return f"software/{instance.file_service}/service_po/{filename}"


def path_file_driver(instance: 'FileSoftware', filename: str) -> str:
    """
    The function generates a path based on the name of the file with the algorithm.

    :param instance: object File
    :param filename: name file
    :return: str - path to save
    """
    return f"software/{instance.file_driver}/driver/{filename}"


def path_file_instruction(instance: 'FileSoftware', filename: str) -> str:
    """
    The function generates a path based on the name of the file with the algorithm.

    :param instance: object File
    :param filename: name file
    :return: str - path to save
    """
    return f"software/{instance.file_service}/file_instruction/{filename}"


class SoftWare(models.Model):
    """
    The Class description the model the software
    """
    name = models.CharField(max_length=100, verbose_name='Наименование')
    slug = models.SlugField(max_length=100, verbose_name='URL', db_index=True)
    access = models.BooleanField(default=True, verbose_name='Доступ')

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        db_table = 'software'
        verbose_name = 'сервис'
        verbose_name_plural = 'сервисы'


class FileSoftware(models.Model):
    """
    The Class description the model the file for software.
    """
    software = models.OneToOneField(SoftWare, on_delete=models.CASCADE, verbose_name='Сервисное ПО')
    file_service = models.FileField(upload_to=path_file_service, verbose_name='Файл ПО')
    file_driver = models.FileField(upload_to=path_file_driver, verbose_name='Драйвер')
    file_instruction = models.FileField(upload_to=path_file_instruction, verbose_name='Инструкция')

    def __str__(self) -> str:
        return f"{self.software}"
    
    class Meta:
        db_table = 'filesoftware'
        verbose_name = 'файл'
        verbose_name_plural = 'файлы'
