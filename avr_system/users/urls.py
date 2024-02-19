from django.urls import path

from .views import (
    ProfileDetailView,
)

app_name = 'users'

urlpatterns = [
    path('account/', ProfileDetailView.as_view(), name='account'),
]
