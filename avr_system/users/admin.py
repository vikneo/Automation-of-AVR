from django.contrib import admin
from django.http import HttpRequest
from django.db.models import QuerySet
from django.utils.safestring import mark_safe

from .models import Profile


@admin.action(description="Добавить в архив")
def added_to_archive(modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet):
    """
    Action to add a user to the archive
    """
    queryset.update(archive=True)


@admin.action(description="Убрать с архива")
def remove_from_archive(modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet):
    """
    Action to delete a user from the archive.
    """
    queryset.update(archive=False)


@admin.register(Profile)
class AdminProfile(admin.ModelAdmin):
    """
    Register the model "Profile" in admin panel
    """
    actions = [
        added_to_archive,
        remove_from_archive,
    ]
    list_display = ['user', 'phone', 'get_avatar', 'archive']
    search_fields = ['user', 'phone']
    list_filter = ['phone', 'user']
    fieldsets = (
        (None, {
            'fields': ('user', 'phone', 'avatar')
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('archive',),
        }),
    )

    def get_avatar(self, obj: Profile) -> str:
        """
        Displaying the user's avatar.
        """
        if obj.avatar:
            return mark_safe(f'<img src="{obj.avatar.url}" width=50>')

    get_avatar.short_description = 'аватар'
