from django.urls import path

from .views import (
    MainPage, 
    TypeAvrDetail,
    HelpView,
    SearcheView,
    OrderView,
    SettingsView,
    SiteName,
    CacheSetupBannerView,
    CacheSetupSystemView
    )

app_name = 'system'

urlpatterns = [
    path('', MainPage.as_view(), name='index'),
    path('detail/<slug:slug>/', TypeAvrDetail.as_view(), name='detail_system'),
    path('helper/', HelpView.as_view(), name='helper'),
    path('search/', SearcheView.as_view(), name='search'),
    path('order/', OrderView.as_view(), name='order'),
    path('settings/', SettingsView.as_view(), name='settings'),
    path('site-name/', SiteName.as_view(), name='site_name'),
    path('cache-time-banner/', CacheSetupBannerView.as_view(), name='cache_time_banner'),
    path('cache-time-system/', CacheSetupSystemView.as_view(), name='cache_time_system'),
]
