from django.db import models
from django.urls import reverse
from core import models as core_models
from users import models as user_models


class Photo(core_models.TimeStampedModel):
    """Photo Model Definition"""

    caption = models.CharField(max_length=100)
    file = models.ImageField(upload_to="store_photos")
    store = models.ForeignKey("Store", on_delete=models.CASCADE)

    def __str__(self):
        return self.caption


class Store(core_models.TimeStampedModel):

    MENU_KOREAN = "korean"
    MENU_WESTERN = "western"
    MENU_CHINESE = "chinese"
    MENU_JAPANESE = "japanese"
    MENU_CAFE = "cafe"
    MENU_ALCOHOL = "alcohol"

    MENU_CHOICES = (
        (MENU_KOREAN, "한식"),
        (MENU_WESTERN, "양식"),
        (MENU_CHINESE, "중식"),
        (MENU_JAPANESE, "일식"),
        (MENU_CAFE, "카페/디저트"),
        (MENU_ALCOHOL, "술집"),
    )

    name = models.CharField(max_length=140, default="")
    address = models.CharField(max_length=140, default="")
    address_detail = models.CharField(max_length=140, default="")
    menu = models.CharField(max_length=100, choices=MENU_CHOICES, null=True, blank=True)
    user = models.ForeignKey(
        user_models.User, verbose_name="사장님", on_delete=models.PROTECT
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("stores:detail", kwargs={"pk": self.pk})

    def total_avg(self):
        all_ratings = self.review_set.all()
        total = 0
        if len(all_ratings) > 0:

            for r in all_ratings:
                total += r.rating_average()
            return total / len(all_ratings)
        return 0
