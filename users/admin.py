from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import CustomUser

# Register your models here.
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ["id", "email", "is_active"]
    list_editable = ["is_active"]
    fieldsets = (
        ("Naruto", {"fields": ("email", "password")}),
        ("Personal info", {"fields": ("is_active", "is_staff", "last_login")}),
    )
    ordering = ("email",)
    search_fields = ["email"]
