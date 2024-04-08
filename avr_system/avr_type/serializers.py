from rest_framework import serializers

from .models import TypeAVR


class TypeAVRSerializers(serializers.ModelSerializer):
    class Meta:
        model = TypeAVR
        fields = '__all__'
