from typing import Any
from django.views.generic import ListView

from utilits.mixins import MenuMixin
from .models import SoftWare


class SoftWareView(MenuMixin, ListView):
    """
    
    """
    model = SoftWare
    template_name = 'software/software_list.html'
    context_object_name = 'services'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context.update(
            self.get_menu(link=4),
            title='Сервисное ПО'
        )
        return context
