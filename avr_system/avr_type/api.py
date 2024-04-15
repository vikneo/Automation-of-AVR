from django.core.cache import cache
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter

from .configs import settings
from .models import (
    TypeAVR,
    Classification,
    SmartRelay,
    )
from .filters import (
    TypeAVRFilter,
    ProductFilter,
    RelayFilter,
    )
from .serializers import (
    TypeAVRSerializers,
    ProductSerializers,
    RelaySerializers,
    )
from .permissions import CustomPermissions


class TypeAVRViewSet(viewsets.ModelViewSet):
    serializer_class = TypeAVRSerializers
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['name', ]
    filter_class = TypeAVRFilter
    permission_classes = (CustomPermissions, )

    def get_queryset(self):
        return cache.get_or_set("systems", TypeAVR.objects.filter(access=True), settings.get_cache_system())


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializers
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['name', ]
    filter_class = ProductFilter
    permission_classes = (CustomPermissions, )

    def get_queryset(self):
        return cache.get_or_set('products', Classification.objects.filter(access=True), settings.get_cache_products())


class RelayViewSet(viewsets.ModelViewSet):
    serializer_class = RelaySerializers
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['model', ]
    filter_class = RelayFilter
    permission_classes = (CustomPermissions, )

    def get_queryset(self):
        return cache.get_or_set('relays', SmartRelay.objects.filter(access=True), 1024)
