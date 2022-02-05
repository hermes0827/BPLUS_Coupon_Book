from django.contrib import admin
from . import models


@admin.register(models.Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ("user", "store", "used", "updated", "used_date")
    fieldsets = (
        (
            None,
            {
                "fields": ("user", "store", "used", "used_date"),
            },
        ),
    )
