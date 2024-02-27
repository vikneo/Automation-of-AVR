


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
            {'name': 'Карта сайта', 'url': 'system:map_site', 'link': 4},
            {'name': 'личный кабинет', 'url': 'system:map_site', 'link': 5},
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
