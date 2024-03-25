from django.urls import path

from .views import SoftWareView


app_name = 'software'

urlpatterns = [
    path('service/', SoftWareView.as_view(), name='service'),
]