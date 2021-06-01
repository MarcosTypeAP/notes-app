from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin

from django.contrib.auth.models import User
from users.models import Profile

# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):

    list_display = ('pk', 'user', 'picture', 'created_at', 'modified_at')
    list_display_links = ('pk', 'user')
    list_editable = ('picture',)

    search_fields = (
        'pk', 
        'user__username', 
        'user__email', 
        'user__first_name', 
        'user__last_name',
    )

    list_filter = (
        'user__is_staff',
        'user__is_superuser',
        'user__is_active',
        'created_at',
        'modified_at',
    )

    fieldsets = (
        ('Profile', {
            'fields': ('user', 'picture'),
        }),
        ('Metadata', {
            'fields': (('created_at', 'modified_at'),)
        })
    )

    readonly_fields = ('created_at', 'modified_at')


class ProfileInline(admin.StackedInline):

    model = Profile
    can_delete = False
    verbose_name_plural = 'profiles'


def deactivate(modeluser, req, queryset):
    queryset.update(is_active=False)


def activate(modeluser, req, queryset):
    queryset.update(is_active=True)


class UserAdmin(BaseUserAdmin):

    inlines = (ProfileInline,)
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_staff',
        'is_active',
    )
    actions = (deactivate, activate)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)