from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    fields = ['username', 'password', 'email']
    list_display = ['id', 'username', 'password', 'email', 'date_joined']


admin.site.register(User, UserAdmin)
