from django.db.models.query import QuerySet
from django.db.models import Q
from django.views.generic import ListView, DetailView, TemplateView
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.contrib import messages
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.core.cache import cache

from .models import TypeAVR, Classification
from utilits.mixins import MenuMixin, ChangeListMixin
from .configs import settings

import re
from typing import Any


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
        
        return cache.get_or_set("systems", TypeAVR.objects.filter(access=True), settings.get_cache_system())


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
            self.get_change_list_admin(),
            title='Настройки'
        )
        return context


class SiteName(ChangeListMixin, TemplateView):
    """
    Класс SiteName позволяет задать новое название интернет магазина
    """

    template_name = 'admin/settings.html'

    def post(self, request) -> HttpResponse:
        title_site = request.POST.get('title_site')
        if title_site:
            settings.set_site_name(title_site)
            messages.success(self.request, _('Название магазина успешно изменено'))
        else:
            messages.warning(self.request, _('Поле не должно быть пустым'))

        return HttpResponseRedirect(reverse_lazy('system:settings'))


class SetCountBanner(ChangeListMixin, TemplateView):
    """
    Установка количеста отображаемых банеров
    """
    template_name = 'admin/settings.html'

    def post(self, request) -> HttpResponse:
        count_banner = request.POST.get('count_banner')
        try:
            num_banner = int(re.findall(r'[0-9]+', count_banner)[0])
            settings.set_count_banner(num_banner)
            messages.success(self.request, f"Установлено {num_banner}шт. банеров.")
        except Exception:
            messages.warning(self.request, _('Поле должно cодержать только цифры'))
        
        return HttpResponseRedirect(reverse_lazy('system:settings'))


class CacheSetupBannerView(ChangeListMixin, TemplateView):
    """
    Класс CacheSetupBannerView позволяет задать или обновить время кэширования Баннера
    """

    template_name = 'admin/settings.html'

    def post(self, request) -> HttpResponse:
        cache_time_banner = request.POST.get('cache_time_banner')
        try:
            time_banner = int(''.join(re.findall(r'[0-9]+', cache_time_banner)))
            if time_banner:
                settings.set_cache_banner(time_banner)
                messages.success(self.request, _('Время кэширование Баннера установлено'))
        except Exception:
            messages.warning(self.request, _('Поле не должно быть пустым или содержать только цифры'))

        return HttpResponseRedirect(reverse_lazy('system:settings'))


class CacheSetupSystemView(ChangeListMixin, TemplateView):
    """
    Класс CacheSetupSystemView позволяет задать или обновить время кэширования типы АВР
    """
    template_name = 'admin/settings.html'

    def post(self, request) -> HttpResponse:
        cache_time_system = request.POST.get('cache_time_system')
        try:
            time_system = int(''.join(re.findall(r'[0-9]+', cache_time_system)))
            settings.set_cache_system(time_system)
            messages.success(self.request, _('Время кэширование для типов АВР установлено'))
        except Exception:
            messages.warning(self.request, _('Поле не должно быть пустым или содержать только цифры'))
        
        return HttpResponseRedirect(reverse_lazy('system:settings'))


class CacheSetupProductView(ChangeListMixin, TemplateView):
    """
    Класс CacheSetupSystemView позволяет задать или обновить время кэширования типы АВР
    """
    template_name = 'admin/settings.html'

    def post(self, request) -> HttpResponse:
        cache_time_product = request.POST.get('cache_time_product')
        try:
            time_product = int(''.join(re.findall(r'[0-9]+', cache_time_product)))
            settings.set_cache_product(time_product)
            messages.success(self.request, _('Время кэширование для классификации продукта установлено'))
        except Exception:
            messages.warning(self.request, _('Поле не должно быть пустым или содержать только цифры'))
        
        return HttpResponseRedirect(reverse_lazy('system:settings'))

# =========================== Настройки по очистке кэша =================================
    
class ClearCacheAll(ChangeListMixin, TemplateView):
    """
    Класс ClearCacheAll позволяет очистить весь кэш сайта
    """

    template_name = 'admin/settings.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        cache.clear()
        messages.success(self.request, _('Кэш полностью очищен.'))

        return context

    def dispatch(self, request, *args, **kwargs) -> HttpResponse:
        if cache:
            super().dispatch(request, *args, **kwargs)

        return HttpResponseRedirect(reverse_lazy("system:settings"))


class ClearCacheBanner(ChangeListMixin, TemplateView):
    """
    Класс ClearCacheBanner позволяет очистить кэш банера
    """

    template_name = 'admin/settings.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        cache.delete('banners')
        messages.success(self.request, _('Кэш банера очищен.'))

        return context

    def dispatch(self, request, *args, **kwargs) -> HttpResponse:
        if cache:
            super().dispatch(request, *args, **kwargs)

        return HttpResponseRedirect(reverse_lazy("system:settings"))
