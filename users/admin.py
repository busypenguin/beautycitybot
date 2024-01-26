from django.contrib import admin
from django.contrib.auth.models import Group

from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'phone_number', )
    search_fields = ('username', )
    empty_value_display = '-пусто-'


admin.site.unregister(Group)
