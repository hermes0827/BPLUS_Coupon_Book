from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    """Custom User Model"""

    username = models.EmailField(unique=True, verbose_name="계정")
    name = models.CharField(verbose_name="이름", max_length=30, default="")
