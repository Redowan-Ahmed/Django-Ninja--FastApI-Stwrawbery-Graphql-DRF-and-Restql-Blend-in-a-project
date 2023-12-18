from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm

    model = CustomUser

    #list_display = ('username', 'email', 'phoneNumber', 'is_active', 'is_staff', 'is_superuser', 'last_login')
    list_filter = ('is_active', 'is_staff', 'is_superuser')
    fieldsets = (
        (None, {'fields': ('first_name', 'last_name',
         'username', 'email', 'phone_number','profile_picture', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
        ('Dates', {'fields': ('last_login', 'date_joined')})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'username', 'email', 'phone_number', 'password1', 'password2', 'is_staff', 'is_active', 'is_superuser')}
         ),
    )
    search_fields = ('email', 'username', 'phone_number')
    ordering = ('email', 'phone_number', 'username', 'last_login')


admin.site.register(CustomUser, CustomUserAdmin)
