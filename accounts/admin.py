from django.contrib import admin
from .models import User

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    modal = User
    fields = ('email', 'password', 'is_active', 'is_staff')
    list_display = ('email','created_at', 'is_staff', 'is_superuser', 'is_active')
    list_filter = ('email', 'is_active', 'is_staff')
    search_fields = ('email',)
    ordering = ('email',)

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff',)}),
    )
    addfieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff',)}),
    )


admin.site.register(User)
