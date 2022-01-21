from django.db import models
from core import models as core_models
from users import models as user_models
from stores import models as store_models


class Coupon(core_models.TimeStampedModel):

    """Coupon Model Definition"""

    updated = models.DateTimeField(verbose_name="사용일자")
    store = models.ForeignKey(store_models.Store, on_delete=models.CASCADE)
