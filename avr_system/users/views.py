from typing import Any
from django.forms import BaseModelForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.core.mail import send_mail
from django.views.generic import DetailView, CreateView, FormView, TemplateView, UpdateView
from django.contrib.auth.views import (
    LoginView, 
    LogoutView, 
    PasswordChangeView, 
    PasswordChangeDoneView
    )

from .models import Profile
from .forms import CallBackForm, UserFormAuth, RegisterUserForm, UserRasswordResetForm
from utilits.mixins import MenuMixin
from avr_system.settings import EMAIL_HOST_USER


class RegisterUserView(MenuMixin, CreateView):
    """
    The registration form
    """
    template_name = 'profile/register.html'
    form_class = RegisterUserForm

    def  get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context.update(
            self.get_menu(),
            title='Регистрация'
        )
        return context

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


class ProfileDetailView(MenuMixin, DetailView):
    """
    Detailed information about the user
    """
    model = Profile
    template_name = 'profile/account.html'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context.update(
            self.get_menu(),
            title='Профиль'
        )
        return context



class UserPasswordResetView(MenuMixin, PasswordChangeView):
    """
    Changing the password
    """
    form_class = UserRasswordResetForm
    success_url = reverse_lazy("users:password_change_done")
    template_name = 'profile/password_reset.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context.update(
            self.get_menu(),
            title='Изменение пароля'
        )

        return context

class UserPasswordChangeDoneView(MenuMixin, PasswordChangeDoneView):
    """
    Confirmation of password change
    """
    template_name = 'profile/password_change_done.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context.update(
            self.get_menu()
        )
        return context


class ContactView(MenuMixin, TemplateView):
    """
    Contact information
    """
    template_name = 'index/contact.html'
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]: 
        context =super().get_context_data(**kwargs)
        context.update(
            self.get_menu(link=3),
            title='Контакты'
        )
        return context


class CallBackView(MenuMixin, FormView):
    """
    The Feedback form
    """
    form_class = CallBackForm
    success_message = 'Ваше письмо успешно отправлено администрации сайта'
    template_name = 'index/call_back.html'
    success_url = reverse_lazy('system:index')

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context.update(
            self.get_menu(link=2),
            title='Обратная связь'
        )
        return context

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        data = form.cleaned_data
        subject = 'Автоматизация систем АВР! (Уточнение или заказ)'
        body = {
            "first_name":"Имя: " + data["first_name"],
            "last_name": "Фамилия: " + data["last_name"],
            "email": "Почта: " + data["email"],
            "message": data['comments']
        }
        message = '\n'.join(body.values())
        send_mail(
            subject=subject,
            message=message,
            from_email=EMAIL_HOST_USER,
            recipient_list=[EMAIL_HOST_USER,]
        )
        messages.success(self.request, 'Ваше письмо успешно отправлено')
        return HttpResponseRedirect(reverse_lazy("system:index"))


class UserLoginView(MenuMixin, LoginView):
    """
    Authorization form
    """
    form_class = UserFormAuth
    template_name = 'profile/login.html'
    success_url = reverse_lazy('system:index')

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context.update(
            self.get_menu(),
            title='Авторизация'
        )
        return context


class UserLogoutView(LogoutView):
    """
    Log out
    """
    next_page = reverse_lazy('system:index')
