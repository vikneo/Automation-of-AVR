from django.contrib import admin
from django.http import HttpRequest
from django.db.models import QuerySet

from .models import SmartRelay, TypeAVR, Classification, File


@admin.action(description='Закрыть доступ')
def close_access(modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet):
    queryset.update(access=False)


@admin.action(description='Открыть доступ')
def open_access(modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet):
    queryset.update(access=True)


class FileTabularInline(admin.TabularInline):
    model = File
    extra = 0


@admin.register(TypeAVR)
class AdminTypeAVR(admin.ModelAdmin):
    """
    Registers model the "TypeAVR" to admin panel
    """
    actions = [
        close_access,
        open_access
    ]
    search_fields = ['name',]
    list_display = ['id', 'name', 'access']
    list_display_links = ['name', ]
    list_filter = ['access', 'name']
    prepopulated_fields = {'slug': ('name', )}


@admin.register(SmartRelay)
class AdminSmartRelay(admin.ModelAdmin):
    """
    Registers model the "SmartRelay" to admin panel
    """
    list_display = ['brend', 'model']
    list_display_links = ['model', ]
    prepopulated_fields = {'slug': ('model', )}


@admin.register(Classification)
class AdminClassification(admin.ModelAdmin):
    """
    Registers model the "Classification" to admin panel
    """
    inlines = [
        FileTabularInline,
    ]
    actions = [
        close_access,
        open_access
    ]
    search_fields = ['name', ]
    list_filter = ['name', 'temp_tp', 'vnr', 'reset', 'shoice_in', 'dgu', 
                   'work_tp', 'status_box', 'lamp_avr_ready', 
                   'lamp_avr_work', 'signal_ozz'
                   ]
    list_display = ['name', 'type_avr', 'access']
    list_display_links = ['name', ]
    prepopulated_fields = {'slug': ('name', )}
    save_on_top = True


@admin.register(File)
class AdminFile(admin.ModelAdmin):
    """
    Registers model the "File" to admin panel
    """
    list_display = ['firmware', 'file']
