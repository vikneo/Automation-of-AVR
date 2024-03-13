from typing import Any
from django.db.models.query import QuerySet
from django.views.generic import ListView, DetailView, TemplateView
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.mixins import PermissionRequiredMixin

from .models import TypeAVR, Classification
from utilits.mixins import MenuMixin, ChangeListMixin


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
        not_found = 'Нет ни одного совпадения'
        try:
            query = self.request.GET.get('search').upper()
            result = Classification.objects.filter(
                Q(name__icontains=query) | 
                Q(relay__model__icontains=query) |
                Q(type_avr__name__startswith=query)
                )
            if not result:
                messages.info(self.request, not_found)
            return result
        except Exception as err:
            messages.info(self.request, not_found)
    

    """
    def get_queryset(self) -> QuerySet[Any]:
        # Search for db postgres
        query = self.request.GET.get('search')
        search_vector = SearchVector('name') + SearchVector('comment')
        search_query = SearchQuery(query)
        return Classification.objects.annotate(rank=SearchRank(search_vector, search_query)).order_by("-rank")
    """


class OrderView(ListView):
    """
    
    """
    pass

# ==================================== Settings in panel admin =========================================

class SettingsView(PermissionRequiredMixin, ChangeListMixin, ListView):
    """
    Класс SettingsView отображает страницу с настройками
    """
    model = Classification
    template_name = 'admin/settings.html'
    permission_required = 'authorization.view_storesettings'

    def  get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context.update(
            self.get_change_list_admin(title='Настройки')
        )
        return context
