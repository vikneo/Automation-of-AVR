from django.contrib import admin
from django.utils.safestring import mark_safe
from django.http import HttpRequest
from django.db.models import QuerySet

from .models import (
    SmartRelay,
    TypeAVR,
    Classification,
    File,
    Banner,
    ImageTypeAVR,
    Advantage,
    Order
)


@admin.action(description='Закрыть доступ')
def close_access(modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet):
    queryset.update(access=False)


@admin.action(description='Открыть доступ')
def open_access(modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet):
    queryset.update(access=True)


class ImageTypeAVRTabular(admin.TabularInline):
    model = ImageTypeAVR
    extra = 0


class FileTabularInline(admin.TabularInline):
    model = File
    extra = 0


@admin.register(TypeAVR)
class AdminTypeAVR(admin.ModelAdmin):
    """
    Registers model the "TypeAVR" to admin panel
    """
    inlines = [
        ImageTypeAVRTabular,
    ]
    actions = [
        close_access,
        open_access
    ]

    search_fields = ['name', ]
    list_display = ['id', 'name', 'get_image', 'access']
    list_display_links = ['name', ]
    list_filter = ['access', 'name']
    prepopulated_fields = {'slug': ('name',)}

    def get_image(self, obj):
        if obj.images.all():
            return mark_safe(f'<img src="{obj.images.last().photo.url}" alt="" width="80">')


@admin.register(SmartRelay)
class AdminSmartRelay(admin.ModelAdmin):
    """
    Registers model the "SmartRelay" to admin panel
    """
    list_display = ['brand', 'model']
    list_display_links = ['model', ]
    prepopulated_fields = {'slug': ('model',)}


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
    list_filter = ['name', 'temp_tp', 'vnr', 'reset', 'choice_in', 'dgu',
                   'work_tp', 'status_box', 'lamp_avr_ready',
                   'lamp_avr_work', 'signal_ozz'
                   ]
    list_display = ['name', 'type_avr', 'macro_code', 'access']
    list_display_links = ['name', ]
    prepopulated_fields = {'slug': ('name',)}
    save_on_top = True


@admin.register(File)
class AdminFile(admin.ModelAdmin):
    """
    Registers model the "File" to admin panel
    """
    list_display = ['firmware', 'file']


@admin.register(Banner)
class AdminBanner(admin.ModelAdmin):
    """
    Registers model the "Banner" to admin panel
    """
    actions = [
        'close_access',
        'open_access'
    ]

    @admin.action(description='Закрыть доступ')
    def close_access(modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet):
        queryset.update(is_active=False)

    @admin.action(description='Открыть доступ')
    def open_access(modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet):
        queryset.update(is_active=True)

    search_fields = ['name', ]
    list_display = ['name', 'create_at', 'is_active', 'get_photo']
    list_filter = ['name', ]
    prepopulated_fields = {'slug': ('name',)}

    def get_photo(self, obj):
        return mark_safe(f'<img src="{obj.photo.url}" alt="" width="60">')

    get_photo.short_description = 'Фото'


@admin.register(Advantage)
class AdminAdvantage(admin.ModelAdmin):
    """
    Registers model the "Advantage" to admin panel
    """
    actions = [
        close_access,
        open_access
    ]
    list_display = ['title', 'get_icon', 'access']
    list_filter = ['title', ]

    def get_icon(self, obj):
        return mark_safe(f'<img src="{obj.icon.url}" alt="" width="30">')

    get_icon.short_description = 'Иконка'


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """
    
    """
    list_display = ['id', 'system', 'name', 'status', 'created_at']
    list_filter = ['name']
