# from django.utils.translation import gettext_lazy as _
from django.contrib import admin

from avr_type.models import Classification
from avr_type.configs import settings


class MenuMixin:
    """
    Класс миксин для навигации по меню
    """

    @staticmethod
    def __menu__() -> list:
        """
        magic method with a menu list.
        :return: list of dictionaries with an available menu.
        :rtype: list
        """
        menu = [
            {'name': 'Главная', 'url': 'system:index', 'link': 1},
            {'name': 'Обратная связь', 'url': 'users:callback', 'link': 2},
            {'name': 'Контакты', 'url': 'users:contact', 'link': 3},
            # {'name': 'Заказы', 'url': 'system:order', 'link': 4},
            {'name': 'Помощь', 'url': 'system:helper', 'link': 5},
            {'name': 'О нас', 'url': 'system:about', 'link': 6},
        ]

        return menu
    
    def get_menu(self, **kwargs) -> dict:
        """
        The method returns the main menu and today's date.
        :param kwargs: accepts the received dictionary.
        :rtype: dict.
        :return: returns the updated dictionary.
        :rtype: dict.
        """
        context = kwargs
        context.update(
            menu=self.__menu__(),
        )

        return context


class ChangeListMixin:
    """
    Класс ChangeListMixin миксуется для отображения "sidebar" и навигации в "header" в шаблоне настроек
    """

    def get_change_list_admin(self, **kwargs):
        model = Classification
        context = kwargs
        context = dict(list(context.items()) + list(admin.site.each_context(self.request).items()))
        context.update(
            opts=model._meta,
            title_site=settings.get_site_name(),
            cache_banner=settings.get_cache_banner(time=False),
            cache_product=settings.get_cache_product_detail(time=False),
            cache_system=settings.get_cache_system(time=False),
            num_banners=settings.get_count_banner(),
            cache_params=settings.get_cache_filter_params(time=False),
            paginate_by = settings.get_paginate_by(),
        )
        return context
