from django.core.cache import cache
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter

from .configs import settings
from .models import TypeAVR, Classification
from .filters import TypeAVRFilter, ProductFilter
from .serializers import TypeAVRSerializers, ProductSerializers
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
