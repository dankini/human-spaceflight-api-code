# apps/common/models.py

from django.db import models


class FullAstronautNameMixin(models.Model):
    """Mixin for full name formatting."""

    class Meta:
        abstract = True  # Prevents Django from creating a table for this

    @property
    def get_full_astronaut_name(self):
        """Returns the full name in format: Lastname, Firstname "Nickname"."""
        last_name = self.last_name
        first_name = self.first_name
        nickname = f' "{self.nick_name}"' if self.nick_name else "" # Places nickname in "" and adds a space before it, if it exists
        return f"{last_name}, {first_name}{nickname}".strip() # Ensures no extra spaces are added to the end of the string
