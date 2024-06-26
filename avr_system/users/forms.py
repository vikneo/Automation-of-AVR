from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.forms import (
    AuthenticationForm,
    PasswordChangeForm,
    UserCreationForm,
)
from django.utils.translation import gettext_lazy as _
from captcha.fields import CaptchaField

from .models import Profile


class UserFormAuth(AuthenticationForm):
    """
    User Authentication Form
    """

    username = forms.CharField(
        label="Логин", widget=forms.TextInput(attrs={"class": "form-input"})
    )
    password = forms.CharField(
        label="Пароль", widget=forms.PasswordInput(attrs={"class": "form-input"})
    )
    error_messages = {
        "invalid_login": _("Комбинация %(username)s и пароля не найдена."),
        "inactive": _("Данный аккаунт заблокирован."),
    }

    def clean_username(self):
        """
        Verification of allowing active users to log in and rejecting inactive users to log in.

        If the given user cannot log in, this method should raise a
        ``ValidationError``.
        """
        username = self.cleaned_data["username"]
        if not User.objects.filter(username=username).exists():
            return username
        if Profile.objects.get(user__username=username).archive:
            raise ValidationError(
                self.error_messages["inactive"],
                code="inactive",
            )

        return username

    class Meta:
        model = User
        fields = ["username", "password"]


class RegisterUserForm(UserCreationForm):
    """
    User Register Form
    """

    username = forms.CharField(
        label=_("Логин"),
        widget=forms.TextInput(
            attrs={"class": "form-input", "placeholder": "Не обязательное поле"},
        ),
    )
    password1 = forms.CharField(
        label=_("Пароль"),
        widget=forms.PasswordInput(
            attrs={
                "class": "form-input",
                "placeholder": "Обязательное поле",
            },
        ),
    )
    password2 = forms.CharField(
        label=_("Повторить пароль"),
        widget=forms.PasswordInput(
            attrs={"class": "form-input", "placeholder": "Обязательное поле"},
        ),
    )
    email = forms.CharField(
        label=_("Почта"),
        widget=forms.EmailInput(
            attrs={"class": "form-input", "placeholder": "Обязательное поле"},
        ),
    )

    """
    def clean_login_field(self):
        login_field = self.cleaned_data['login_field']
        if re.search(r'(\+7|8)\D*\d{3}\D*\d{3}\D*\d{2}\D*\d{2}', login_field):
            if Profile.objects.filter(phone=login_field).exists():
                raise forms.ValidationError("Такой телефон уже существует")
        elif re.search(r'', login_field):
            if User.objects.filter(email=login_field).exists():
                raise forms.ValidationError("Данный email уже существует.")

        return login_field
    """

    def clean_phone(self):
        phone = self.cleaned_data["phone"]
        if Profile.objects.filter(phone=phone).exists():
            raise forms.ValidationError("Такой телефон уже существует")
        return phone

    def clean_username(self):
        username = self.cleaned_data["username"]
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Такой логин уже существует")

        return username

    def clean_email(self):
        email = self.cleaned_data["email"]
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Данный email уже существует.")

        return email

    def clean_password2(self):
        passw1 = self.cleaned_data["password1"]
        passw2 = self.cleaned_data["password2"]
        if passw1 != passw2:
            raise forms.ValidationError("Пароли не совпадают")
        if len(passw1) < 6:
            raise forms.ValidationError("Пароль должен содержать не менее 6 символов")

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class UserRasswordResetForm(PasswordChangeForm):
    """ """

    old_password = forms.CharField(
        label="Старый пароль", widget=forms.PasswordInput(attrs={"class": "form-input"})
    )
    new_password1 = forms.CharField(
        label="Новый пароль", widget=forms.PasswordInput(attrs={"class": "form-input"})
    )
    new_password2 = forms.CharField(
        label="Подтверждение пароля",
        widget=forms.PasswordInput(attrs={"class": "form-input"}),
    )


class ProfileUpdateForm(forms.ModelForm):
    """ """
    username = forms.CharField(
        label="Логин",
        widget=forms.TextInput(attrs={"class": "form-input"}),
        required=False,
    )
    first_name = forms.CharField(
        label="Имя",
        widget=forms.TextInput(attrs={"class": "form-input"}),
        required=False,
    )
    last_name = forms.CharField(
        label="Фамилия",
        widget=forms.TextInput(attrs={"class": "form-input"}),
        required=False,
    )
    email = forms.CharField(
        label="Почта",
        widget=forms.EmailInput(attrs={"class": "form-input"}),
        required=False,
    )
    phone = forms.CharField(
        label="Телефон",
        widget=forms.TextInput(attrs={"class": "form-input"}),
        required=False,
    )
    avatar = forms.ImageField(
        label="Аватар",
        widget=forms.FileInput(
            attrs={
                "class": "form-input",
                "id": "avatar",
                "name": "avatar",
                "type": "file",
                "enctype": "multipart/form-data",
            },
        ),
        required=False,
    )

    class Meta:
        model = Profile
        fields = ["username", "first_name", "last_name", "avatar", "phone"]


class CallBackForm(forms.Form):
    """
    
    """
    first_name = forms.CharField(
        label="Имя",
        widget=forms.TextInput(attrs={"class": "form-input", "placeholder": "Имя"}),
    )
    last_name = forms.CharField(
        label="Фамилия",
        widget=forms.TextInput(attrs={"class": "form-input", "placeholder": "Фамилия"}),
    )
    email = forms.CharField(
        label="Почта",
        widget=forms.EmailInput(attrs={"class": "form-input", "placeholder": "Email"}),
    )
    comments = forms.CharField(
        label="Текст сообщения",
        widget=forms.Textarea(
            attrs={"class": "form-input", "rows": "6", "placeholder": "Текст сообщения"}
        ),
    )
    captcha = CaptchaField(label='Капча')

    class Meta:
        fields = ["first_name", "last_name", "email", "comment"]
