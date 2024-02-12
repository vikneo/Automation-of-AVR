from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Profile


@admin.register(Profile)
class AdminProfile(admin.ModelAdmin):
    """
    Register the model "Profile" in admin panel
    """
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
        
        """
        if obj.avatar:
            return mark_safe(f'<img src="{obj.avatar.url}">')
    
    get_avatar.short_description = 'аватар'
