from django_filters.rest_framework import CharFilter, FilterSet

from .models import TypeAVR


class TypeAVRFilter(FilterSet):

    name = CharFilter(field_name='name', lookup_expr='startswith', label='Тип АВР')

    class Meta:
        model = TypeAVR
        fields = ['name']
