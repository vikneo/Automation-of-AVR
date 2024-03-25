from django.apps import AppConfig


class SoftwareConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'software'
    verbose_name = 'сирвисное по'

    def ready(self) -> None:
        import users.signals
