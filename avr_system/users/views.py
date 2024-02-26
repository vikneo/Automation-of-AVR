from typing import Any
from django.forms import BaseModelForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.core.mail import send_mail
from django.views.generic import ListView, DetailView, CreateView, FormView
from django.contrib.auth.views import LoginView, LogoutView

from .models import Profile
from .forms import CallBackForm, UserFormAuth, RegisterUserForm


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


class CallBackView(FormView):
    """
    
    """
    form_class = CallBackForm
    success_message = 'Ваше письмо успешно отправлено администрации сайта'
    template_name = 'index/call_back.html'
    success_url = reverse_lazy('system:index')

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context.update(
            title='Обратная связь'
        )
        return context

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        data = form.cleaned_data
        subject = f'Сообщение от {data["first_name"]} {data["last_name"]} Почта отправителя: {data["email"]}'
        send_mail(
            subject=subject,
            message=data['comments'],
            from_email='v.martynov@rineco.ru',
            recipient_list=[data['email']]
        )
        
        return HttpResponseRedirect(reverse_lazy("system:index"))


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
