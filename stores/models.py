from django.db import models
from core import models as core_models


class Store(core_models.TimeStampedModel):

    name = models.CharField(max_length=140)
    address = models.CharField(max_length=140)
