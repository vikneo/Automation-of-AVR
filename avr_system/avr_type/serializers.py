from rest_framework import serializers

from .models import TypeAVR, Classification


class TypeAVRSerializers(serializers.ModelSerializer):
    class Meta:
        model = TypeAVR
        fields = '__all__'


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Classification
        fields = [
            'id',
            'type_avr',
            'name',
            'slug',
            'vnr',
            'temp_tp',
            'reset',
            'choice_in',
            'dgu',
            'work_tp',
            'status_box',
            'lamp_avr_ready',
            'lamp_avr_work',
            'signal_ozz',
            'comment',
            'relay',
        ]
