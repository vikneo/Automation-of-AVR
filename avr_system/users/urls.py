from django.urls import path

from .views import (
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
)

app_name = 'users'

urlpatterns = [
    path('account/<int:pk>/', ProfileDetailView.as_view(), name='account'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('register/', RegisterUserView.as_view(), name='register'),
    path('update/<int:pk>/', ProfileUpdateVIew.as_view(), name='update'),
    path('password-change/', UserPasswordChangeView.as_view(), name='password_change'),
    path('password-change/done/', UserPasswordChangeDoneView.as_view(), name="password_change_done"),
    path('password-reset/', UserPasswordResetView.as_view(), name='password_reset'),

    path('callback/', CallBackView.as_view(), name='callback'),
    path('contact/', ContactView.as_view(), name='contact')
]
