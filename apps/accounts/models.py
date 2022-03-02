# apps/accounts/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """Class docstring."""

    pass
