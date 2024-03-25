from django.apps import AppConfig


class AvrTypeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'avr_type'
    verbose_name = 'системы авр'

    def ready(self) -> None:
        import avr_type.signals
