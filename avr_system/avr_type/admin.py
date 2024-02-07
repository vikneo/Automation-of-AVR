from django.contrib import admin

from .models import SmartRelay, TypeAVR, Classification, File


@admin.register(TypeAVR)
class AdminTypeAVR(admin.ModelAdmin):
    """
    Registers model the "TypeAVR" to admin panel
    """
    list_display = ['id', 'name']


@admin.register(SmartRelay)
class AdminSmartRelay(admin.ModelAdmin):
    """
    Registers model the "SmartRelay" to admin panel
    """
    list_display = ['brend', 'model']


@admin.register(Classification)
class AdminClassification(admin.ModelAdmin):
    """
    Registers model the "Classification" to admin panel
    """
    list_display = ['name', ]


@admin.register(File)
class AdminFile(admin.ModelAdmin):
    """
    Registers model the "File" to admin panel
    """
    list_display = ['firmware', 'file']