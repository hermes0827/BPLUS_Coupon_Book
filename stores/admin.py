from django.contrib import admin
from . import models


class PhotoInline(admin.TabularInline):
    model = models.Photo


@admin.register(models.Store)
class StoreAdmin(admin.ModelAdmin):

    inlines = (PhotoInline,)

    list_display = (
        "name",
        "address",
        "address_detail",
        "menu",
        "user",
        "total_avg",
    )
    list_filter = ("menu",)

    raw_id_fields = ("user",)
