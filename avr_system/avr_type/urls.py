from django.urls import path

from .views import (
    MainPage, 
    TypeAvrDetail,
    HelpView,
    ContactsView
    )

app_name = 'system'

urlpatterns = [
    path('', MainPage.as_view(), name='index'),
    path('detail/<slug:slug>/', TypeAvrDetail.as_view(), name='detail_system'),
    path('helper/', HelpView.as_view(), name='helper'),
    path('contacts/', HelpView.as_view(), name='contact'),
]
