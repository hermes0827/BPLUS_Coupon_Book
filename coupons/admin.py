from django.contrib import admin
from . import models


@admin.register(models.Coupon)
class CouponAdmin(admin.ModelAdmin):
    pass
