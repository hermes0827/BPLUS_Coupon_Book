from django.db import models
from core import models as core_models


class Review(core_models.TimeStampedModel):

    """Review Model Definition"""

    REVIEW_CHOICES = [(i, i) for i in range(1, 6)]

    kindness = models.IntegerField(verbose_name="친절도", choices=REVIEW_CHOICES)
    cleanliness = models.IntegerField(verbose_name="청결도", choices=REVIEW_CHOICES)
    location = models.IntegerField(verbose_name="접근성", choices=REVIEW_CHOICES)
    deliciousness = models.IntegerField(verbose_name="맛", choices=REVIEW_CHOICES)
    user = models.ForeignKey("users.User", verbose_name="리뷰어", on_delete=models.CASCADE)
    store = models.ForeignKey(
        "stores.Store", verbose_name="가게", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.store.name} - {self.user.username}"

    def rating_average(self):
        avg = (
            self.kindness + self.cleanliness + self.location + self.deliciousness
        ) / 4

        return round(avg, 2)
