from django.db import models
from django.utils import timezone
from core import models as core_models
from stores import models as store_models


class Coupon(core_models.TimeStampedModel):

    """Coupon Model Definition"""

    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    store = models.ForeignKey(store_models.Store, on_delete=models.CASCADE)
    used_date = models.DateTimeField(verbose_name="사용일자", null=True, blank=True)
    used = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.used:
            pass
        else:
            super().save(*args, **kwargs)
