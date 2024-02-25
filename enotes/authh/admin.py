from django.contrib import admin

from .models import Signup

# Register your models here.

class SignupAdmin(admin.ModelAdmin):
    list_display = ('user', 'ContactNo', 'About', 'Role', 'RegDate')
    search_fields = ('user__username', 'ContactNo', 'About', 'Role')
    list_filter = ('RegDate',)

    fieldsets = (
        (None, {
            'fields': ('user',)
        }),
        ('Additional Information', {
            'fields': ('ContactNo', 'About', 'Role')
        }),
    )

admin.site.register(Signup, SignupAdmin)


