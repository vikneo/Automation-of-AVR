from avr_type.configs import settings


def system(request):
    """
    Контекстный процессор позволяет воспользоваться переменными "mount"
    для вывода даты в шаблонах сайта.
    """
    return {
        'mount': settings,
    }
