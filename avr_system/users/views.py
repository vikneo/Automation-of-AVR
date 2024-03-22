from typing import Any
from django.forms import BaseModelForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.views.generic import ListView, DetailView, CreateView, FormView, TemplateView, UpdateView
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordChangeView,
    PasswordChangeDoneView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)

from .models import Profile
from .forms import (
    CallBackForm,
    UserFormAuth,
    RegisterUserForm,
    UserRasswordResetForm,
    ProfileUpdateForm
)
from avr_type.models import Order
from utilits.mixins import MenuMixin
from avr_system.settings import EMAIL_HOST_USER


class AdministrationView(MenuMixin, ListView):
    """
    Displaying all orders
    """
    model = Order
    template_name = 'profile/admin.html'
    paginate_by = 10
    context_object_name = 'orders'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context.update(
            self.get_menu(),
            title='Администратор'
        )
        return context


class RegisterUserView(MenuMixin, CreateView):
    """
    The registration form
    """
    template_name = 'profile/register.html'
    form_class = RegisterUserForm

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
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


class ProfileUpdateVIew(MenuMixin, UpdateView):
    """
    Updating profile data
    """
    model = User
    form_class = ProfileUpdateForm
    template_name = 'profile/update.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context.update(
            self.get_menu(),
            form=self.get_data,
            title='Редактирование профиля'
        )

        return context

    def get_profile_user(self):
        user = self.request.user
        profile = Profile.objects.get(user=user)

        return user, profile

    def get_data(self):
        user, profile = self.get_profile_user()
        data = {
            'email': user.email, 'first_name': user.first_name,
            'last_name': user.last_name, 'phone': profile.phone,
            'avatar': profile.avatar
        }
        form = ProfileUpdateForm(data)

        return form

    def get_success_url(self) -> str:
        return reverse_lazy('users:account', kwargs={'pk': self.request.user.id})

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        user, profile = self.get_profile_user()
        user.first_name = form.cleaned_data['first_name']
        user.last_name = form.cleaned_data['last_name']
        user.email = form.cleaned_data['email']
        user.save()

        profile.phone = form.cleaned_data['phone']
        if form.cleaned_data['avatar']:
            profile.avatar = form.cleaned_data['avatar']
        profile.save()

        return super().form_valid(form)


class UserPasswordChangeView(MenuMixin, PasswordChangeView):
    """
    Changing the password
    """
    form_class = UserRasswordResetForm
    success_url = reverse_lazy("users:password_change_done")
    template_name = 'profile/password_change.html'

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


class UserPasswordResetView(MenuMixin, PasswordResetView):
    """
    Reset password
    """
    template_name = 'registration/password_reset.html'

    def get_context_data(self, **kwargs: Any) -> Any:
        context = super().get_context_data(**kwargs)
        context.update(
            self.get_menu()
        )
        return context


class UserPasswordResetDoneView(MenuMixin, PasswordResetDoneView):
    """
    Password reset done
    """
    template_name = 'registration/password_reset_done.html'

    def get_context_data(self, **kwargs: Any) -> Any:
        context = super().get_context_data(**kwargs)
        context.update(
            self.get_menu()
        )
        return context


class UserPasswordResetConfirmView(MenuMixin, PasswordResetConfirmView):
    """
    Password reset confirm
    """
    template_name = 'registration/password_reset_confirm.html'

    def get_context_data(self, **kwargs: Any) -> Any:
        context = super().get_context_data(**kwargs)
        context.update(
            self.get_menu(),
        )
        return context


class UserPasswordResetCompleteView(MenuMixin, PasswordResetCompleteView):
    """
    Password reset complete
    """
    template_name = 'registration/password_reset_complete.html'

    def get_context_data(self, **kwargs: Any) -> Any:
        context = super().get_context_data(**kwargs)
        context.update(
            self.get_menu(),
        )
        return context


class ContactView(MenuMixin, TemplateView):
    """
    Contact information
    """
    template_name = 'index/contact.html'
    success_url = reverse_lazy('users:password_reset_confirm')

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
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
            "first_name": "Имя: " + data["first_name"],
            "last_name": "Фамилия: " + data["last_name"],
            "email": "Почта: " + data["email"],
            "message": data['comments']
        }
        message = '\n'.join(body.values())
        send_mail(
            subject=subject,
            message=message,
            from_email=EMAIL_HOST_USER,
            recipient_list=[EMAIL_HOST_USER, ]
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
