from django.urls import path

from .views import (
    ProfileDetailView,
    UserLoginView,
    UserLogoutView,
    RegisterUserView,
)

app_name = 'users'

urlpatterns = [
    path('account/', ProfileDetailView.as_view(), name='account'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('register/', RegisterUserView.as_view(), name='register'),
]
