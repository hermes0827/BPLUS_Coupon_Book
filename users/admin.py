from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    """Custom User Admin"""

    list_display = ("username",)
    fieldsets = (
        (
            None,
            {
                "fields": ("username", "name"),
            },
        ),
    )
