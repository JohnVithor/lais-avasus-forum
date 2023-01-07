from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.

from .forms import RegisterForm, UserAdminCreationForm, UserAdminChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = UserAdminCreationForm
    form = UserAdminChangeForm
    model = CustomUser
    list_display = ('cpf', 'name', 'social_name', 'birth_date', 'is_professor', 'state', 'city')
    list_filter = ('cpf', 'name', 'social_name', 'birth_date')
    fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('cpf', 'name', 'social_name', 'birth_date', 'state', 'city', 'password', 'is_professor', 'is_active')}
        ),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('cpf', 'name', 'social_name', 'birth_date', 'state', 'city', 'password', 'password_2', 'is_professor', 'is_active')}
        ),
    )
    search_fields = ('cpf', 'name', 'social_name')
    ordering = ('name', 'birth_date')


admin.site.register(CustomUser, CustomUserAdmin)