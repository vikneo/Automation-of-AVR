from django_filters.rest_framework import CharFilter, FilterSet

from .models import TypeAVR, Classification


class TypeAVRFilter(FilterSet):

    name = CharFilter(field_name='name', lookup_expr='startswith', label='Тип АВР')

    class Meta:
        model = TypeAVR
        fields = ['name']


class ProductFilter(FilterSet):

    name = CharFilter(field_name='name', lookup_expr='startswith', label='Классификация')

    class Meta:
        model = Classification
        fields = ['name', 'type_avr']
