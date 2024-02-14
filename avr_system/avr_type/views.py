from typing import Any
from django.shortcuts import render
from django.views.generic import ListView

from .models import TypeAVR


class MainPage(ListView):
    """
    The system_avr main page view and display class.
    """
    model = TypeAVR
    template_name = 'index/system_avr.html'
    context_object_name = 'systems'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context.update(
            title='Системы АВР'
        )
        return context

