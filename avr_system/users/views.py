from typing import Any
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.contrib.auth.views import LoginView, LogoutView

from .models import Profile


class ProfileDetailView(ListView):
    """
    
    """
    model = Profile
    template_name = 'profile/account.html'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context.update(
            title='Профиль'
        )
        return context


class UserLoginView(LoginView):
    """
    
    """
    form_class = AuthenticationForm
    template_name = 'profile/login.html'
    success_url = reverse_lazy('users:account')

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context.update(
            title='Авторизация'
        )
        return context


class UserLogoutView(LogoutView):
    """
    
    """
    next_page = '/'
    # next_page = reverse_lazy('system:index')
