from django.urls import path

from .views import (
    MainPage,
    TypeAvrDetail,
    HelpView,
    AboutView,
    SearcheView,
    OrderView,
    SettingsView,
    SiteName,
    SetCountBanner,
    CacheSetupBannerView,
    CacheSetupSystemView,
    CacheSetupProductView,
    ClearCacheAll,
    ClearCacheBanner,
    ClearCacheSystem,
    ClearCacheProduct,
    OrderView,
    OrderDetailView,
    )

app_name = 'system'

urlpatterns = [
    path('', MainPage.as_view(), name='index'),
    path('detail/<slug:slug>/', TypeAvrDetail.as_view(), name='detail_system'),
    path('helper/', HelpView.as_view(), name='helper'),
    path('about/', AboutView.as_view(), name='about'),
    path('search/', SearcheView.as_view(), name='search'),
    path('order/', OrderView.as_view(), name='order'),
    path('order-history/', OrderDetailView.as_view(), name='order_history'),
    path('settings/', SettingsView.as_view(), name='settings'),
    path('site-name/', SiteName.as_view(), name='site_name'),
    path('cache-time-banner/', CacheSetupBannerView.as_view(), name='cache_time_banner'),
    path('cache-time-system/', CacheSetupSystemView.as_view(), name='cache_time_system'),
    path('cache-time-product/', CacheSetupProductView.as_view(), name='cache_time_product'),
    path('set-count-banner/', SetCountBanner.as_view(), name='set_count_banner'),
    path('clear-cache-all', ClearCacheAll.as_view(), name='clear_cache_all'),
    path('clear-cache-banner', ClearCacheBanner.as_view(), name='clear_cache_banner'),
    path('clear-cache-system', ClearCacheSystem.as_view(), name='clear_cache_system'),
    path('clear-cache-product', ClearCacheProduct.as_view(), name='clear_cache_product'),
]
