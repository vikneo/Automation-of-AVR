from django.urls import path, include

from .views import (
    AdministrationView,
    ProfileDetailView,
    UserLoginView,
    UserLogoutView,
    RegisterUserView,
    CallBackView,
    ContactView,
    UserPasswordChangeView,
    UserPasswordChangeDoneView,
    ProfileUpdateVIew,
    UserPasswordResetView,
    UserPasswordResetDoneView,
    UserPasswordResetConfirmView,
    UserPasswordResetCompleteView,
)

app_name = 'users'

urlpatterns = [
    path('password-reset/', UserPasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/',
         UserPasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         UserPasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         UserPasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
         name='password_reset_complete'),
    path('account/<int:pk>/', ProfileDetailView.as_view(), name='account'),
    path('account/<int:pk>/admin/', AdministrationView.as_view(), name='admin'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('register/', RegisterUserView.as_view(), name='register'),
    path('update/<int:pk>/', ProfileUpdateVIew.as_view(), name='update'),
    path('password-change/', UserPasswordChangeView.as_view(), name='password_change'),
    path('password-change/done/', UserPasswordChangeDoneView.as_view(), name="password_change_done"),
    path('callback/', CallBackView.as_view(), name='callback'),
    path('contact/', ContactView.as_view(), name='contact')
]
