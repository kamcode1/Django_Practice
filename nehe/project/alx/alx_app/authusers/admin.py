from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as CustomUserAdmin
from .models import User
# Register your models here.
class UserAdmin(CustomUserAdmin):
    list_display = ("email", "is_staffhttp://127.0.0.1:8000/")
admin.site.register(User, UserAdmin)