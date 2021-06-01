from django.contrib import admin

from notes.models import Note


def deactivate(modelnote, req, queryset):
    queryset.update(is_active=False)


def activate(modelnote, req, queryset):
    queryset.update(is_active=True)

@admin.register(Note)
class NotesAdmin(admin.ModelAdmin):

    list_display = ('pk', 'user', 'title', 'created_at', 'modified_at', 'is_active')
    list_display_links = ('pk', 'title')
    list_editable = ('user',)

    search_fields = ('pk', 'title', 'user')

    list_filter = ('is_active', 'created_at', 'modified_at')

    fieldsets = (
        ('Owner ', {
            'fields': ('user',)
        }),
        ('Content', {
            'fields': ('title', 'content')
        }),
        ('Metadata', {
            'fields': ('created_at', 'modified_at')
        })
    )

    readonly_fields = ('created_at', 'modified_at')

    actions = (deactivate, activate)


# admin.site.unregister(Note)
# admin.site.register(Note, NoteAdmin)