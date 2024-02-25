from django.contrib import admin
from .models import *

# Register your models here.

from django.contrib import admin
from .models import Notes

class NotesAdmin(admin.ModelAdmin):
    list_display = ('Title', 'signup', 'CreationDate', 'UpdationDate', 'publish')
    search_fields = ('Title', 'Content', 'signup__user__username')
    list_filter = ('CreationDate', 'UpdationDate', 'publish')
    date_hierarchy = 'CreationDate'

    fieldsets = (
        (None, {
            'fields': ('Title', 'Content', 'signup')
        }),
        ('Date Information', {
            'fields': ('CreationDate', 'UpdationDate')
        }),
        ('Publish', {
            'fields': ('publish',)
        }),
    )

admin.site.register(Notes, NotesAdmin)


