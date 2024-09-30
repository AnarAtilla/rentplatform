from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from .forms import CustomUserCreationForm, UserProfileForm

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = UserProfileForm
    model = User
    list_display = ['email', 'is_landlord', 'is_business_account', 'status', 'date_joined']
    list_filter = ['is_landlord', 'is_business_account', 'status']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('company_name', 'address', 'phone_number', 'additional_contact_info')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'groups', 'user_permissions')}),
        ('Status', {'fields': ('status',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_landlord', 'company_name', 'address', 'phone_number', 'additional_contact_info'),
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)

admin.site.register(User, CustomUserAdmin)
