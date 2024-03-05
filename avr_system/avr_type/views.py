import re
from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank

from .models import TypeAVR, Classification
from utilits.mixins import MenuMixin


class MainPage(MenuMixin, ListView):
    """
    The system_avr main page view and display class.
    """
    template_name = 'index/system_avr.html'
    context_object_name = 'systems'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context.update(
            self.get_menu(link=1),
            title='Главная'
        )
        return context

    def get_queryset(self) -> QuerySet[Any]:
        return TypeAVR.objects.filter(access=True)


class TypeAvrDetail(MenuMixin, DetailView):
    """
    The system_avr class for viewing and displaying detailed information.
    """
    template_name = 'index/detail_system.html'
    context_object_name = 'system'

    def  get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context.update(
            self.get_menu(),
            title='Типы АВР'
        )
        return context
    
    def get_queryset(self) -> QuerySet[Any]:
        return TypeAVR.objects.filter(access=True)


class HelpView(MenuMixin, TemplateView):
    """
    Template rresentation "HelpView"
    """
    template_name = 'index/helper.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context.update(
            self.get_menu(link=5),
            title='Помощь'
        )
        return context


class SearcheView(MenuMixin, ListView):
    """
    The search engine
    """
    # model = Classification
    template_name = 'index/search.html'
    context_object_name = 'searches'
    paginate_by = 10
    allow_empty = True

    def  get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context.update(
            self.get_menu(),
            title=f"Результат поиска - {self.request.GET.get('search')}"
        )
        return context
    
    def get_queryset(self) -> QuerySet[Any]:
        query = self.request.GET.get('search')
        return self.get_search_field( query)
    
    @staticmethod
    def get_search_field(query: str) -> list:
        """
        Search for the value in the "name" and "comment" fields of the "Classification" model
        """
        product_list = []
        for result in Classification.objects.all():

            if re.findall(fr'{query}', result.name) or re.findall(fr'{query}', result.comment):
                product_list.append(result)
        
        return product_list

    """

    def get_queryset(self) -> QuerySet[Any]:
        # Search for db postgres
        query = self.request.GET.get('search')
        search_vector = SearchVector('name') + SearchVector('comment')
        search_query = SearchQuery(query)
        return Classification.objects.annotate(rank=SearchRank(search_vector, search_query)).order_by("-rank")
    """
