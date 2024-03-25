from typing import Any
from django.views.generic import TemplateView

from utilits.mixins import MenuMixin


class SoftWareView(MenuMixin, TemplateView):
    """
    
    """
    template_name = 'software/software_list.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context.update(
            self.get_menu(link=4),
            title='Сервисное ПО'
        )
        return context
