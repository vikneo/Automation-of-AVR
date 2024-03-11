from django.urls import path

from .views import (
    MainPage, 
    TypeAvrDetail,
    HelpView,
    SearcheView,
    OrderView,
    )

app_name = 'system'

urlpatterns = [
    path('', MainPage.as_view(), name='index'),
    path('detail/<slug:slug>/', TypeAvrDetail.as_view(), name='detail_system'),
    path('helper/', HelpView.as_view(), name='helper'),
    path('search/', SearcheView.as_view(), name='search'),
    path('order/', OrderView.as_view(), name='order'),
]
