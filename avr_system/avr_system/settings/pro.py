from .base import *


DEBUG = os.getenv("DEBUG", False)

ADMINS = (("Martynov Viktor", "test@test.com"),)

ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS")

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": os.getenv("DB_ENGINE"),
        "NAME": os.getenv("DB_NAME"),
        "USER": os.getenv("DB_USER"),
        "PASSWORD": os.getenv("DB_PASSWORD"),
        "HOST": os.getenv("DB_HOST"),
    }
}
