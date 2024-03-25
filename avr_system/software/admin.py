from django.contrib import admin
from django.http import HttpRequest
from django.db.models import QuerySet

from .models import SoftWare, FileSoftware


@admin.action(description='Закрыть доступ')
def close_access(modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet):
    queryset.update(access=False)


@admin.action(description='Открыть доступ')
def open_access(modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet):
    queryset.update(access=True)


class FileSoftTabularInline(admin.TabularInline):

    model = FileSoftware
    extra = 0


@admin.register(SoftWare)
class AdminSoftWare(admin.ModelAdmin):
    """
    
    """
    inlines = [FileSoftTabularInline, ]
    actions = [
        close_access,
        open_access
    ]

    list_display = ['id', 'name', 'access']
    list_display_links = ['name',]
    list_filter = ['name', ]
    search_fields = ['name',]
    prepopulated_fields = {'slug': ('name',)}
