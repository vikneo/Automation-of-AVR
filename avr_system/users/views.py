from typing import Any
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.views import LoginView, LogoutView

from .models import Profile
from .forms import UserFormAuth, RegisterUserForm


class RegisterUserView(CreateView):
    """
    
    """
    template_name = 'profile/register.html'
    form_class = RegisterUserForm

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        user = form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        email = form.cleaned_data.get('email')
        Profile.objects.create(
            user=user,
        )
        user = authenticate(username=username, password=password)
        login(self.request, user)

        return redirect(reverse_lazy('system:index'))


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
    form_class = UserFormAuth
    template_name = 'profile/login.html'
    success_url = reverse_lazy('system:index')

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context.update(
            title='Авторизация'
        )
        return context


class UserLogoutView(LogoutView):
    """
    
    """
    next_page = reverse_lazy('system:index')
