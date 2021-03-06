from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    """Custom User Admin"""

    list_display = ("email", "name", "login_method", "email_verified")
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "name",
                    "email",
                    "login_method",
                    "email_verified",
                    "email_secret",
                    "is_superuser",
                ),
            },
        ),
    )
