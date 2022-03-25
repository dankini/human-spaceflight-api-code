# apps/agencies/models.py
import uuid
from django.db import models
from django.urls import reverse


class Agency(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    abbreviation = models.CharField(max_length=20)
    country = models.CharField(max_length=50, blank=True)
    formed_date = models.DateField(
        auto_now=False, auto_now_add=False, null=True, blank=True
    )
    website = models.URLField(max_length=100, blank=True)

    class Meta:
        verbose_name_plural = "Agencies"

    def __str__(self):
        return self.abbreviation

    def get_absolute_url(self):
        return reverse("agency_detail", args=[str(self.id)])
