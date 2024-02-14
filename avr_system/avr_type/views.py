from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, DetailView

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

class TypeAvrDetail(DetailView):
    """
    
    """
    template_name = 'index/detail_system.html'
    context_object_name = 'system'

    def  get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context.update(
            title='Detail'
        )
        return context
    
    def get_queryset(self) -> QuerySet[Any]:
        return TypeAVR.objects.filter(access=True)
