from django import template
from django.http import HttpResponse
from django.core.cache import cache

from ..models import Banner
from ..configs import settings

register = template.Library()


@register.inclusion_tag('banner/banner_tpl_main.html')
def banner_main_page() -> dict:
    """
    Caching of three banners is created.
    """
    try:
        banners = cache.get_or_set('banners', Banner.objects.filter(is_active=True), settings.get_cache_banner())
        return {'banners': banners[:settings.get_count_banner]}
    except Exception as err:
        HttpResponse('Not Banners', err)  # TODO заменить заглушку на файл с логами
