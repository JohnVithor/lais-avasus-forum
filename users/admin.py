from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.

from .forms import RegisterForm, UserAdminCreationForm, UserAdminChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = UserAdminCreationForm
    form = UserAdminChangeForm
    model = CustomUser
    list_display = ('cpf', 'name', 'social_name', 'birth_date', 'is_staff', 'state', 'city')
    list_filter = ('cpf', 'name', 'social_name')
    fieldsets = (
        (None, {'fields': ('cpf', 'name', 'social_name', 'birth_date', 'state', 'city', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('cpf', 'password', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('cpf', 'name', 'social_name')
    ordering = ('name',)


admin.site.register(CustomUser, CustomUserAdmin)