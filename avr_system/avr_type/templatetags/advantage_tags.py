from django import template
from django.http import HttpResponse
from django.core.cache import cache

from ..models import Advantage

register = template.Library()

@register.inclusion_tag('advantage/advantage_main.html')
def advantage_main_page():
    """
    
    """
    try:
        advantages = cache.get_or_set('advantages', Advantage.objects.filter(access=True), 600)
        return {'advantages': advantages}
    except Exception as err:
        HttpResponse('Not Advantages', err)
