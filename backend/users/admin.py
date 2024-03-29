from django.contrib import admin

import api.constant
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'id')
    list_filter = ('email', 'username')
    empty_value_display = api.constant.EMPTY_VALUE_DISPLAY
