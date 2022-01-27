from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm
from .models import User

class MyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User

class MyUserAdmin(UserAdmin):
    form = MyUserChangeForm
    ordering = ('email',)
    list_display = ('email', 'username', 'first_name', 'last_name', 'is_staff')

    fieldsets = (
        ('User Information', {'fields': ('email', 'username', 'first_name', 'last_name',)}),
        ('Programs', {'fields': ('employment_supports', 'day_hab', 'specialized_supports', 'cbds',)}),
        ('Permissions', {'fields': ('is_staff', 'is_admin',)}),
        ('User Role', {'fields': ('role',)}),
        ('Date Joined', {'fields': ('date_joined',)}),
    )

admin.site.unregister(Group)
admin.site.register(User, MyUserAdmin)
