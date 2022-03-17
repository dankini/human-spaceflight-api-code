# apps/evas/models.py

import uuid
from django.db import models
from django.urls import reverse

# eva type choices drop-down list
STANDUP = "SU"
SPACEWALK = "SW"
MOONWALK = "MW"
TYPE_CHOICES = [
    (STANDUP, "Stand-up"),
    (SPACEWALK, "Spacewalk"),
    (MOONWALK, "Moonwalk"),
]

# tethered/untethered drop-down list
TETHERED = "TE"
UNTETHERED = "UT"
TETHERED_CHOICES = [
    (TETHERED, "Tethered"),
    (UNTETHERED, "Untethered"),
]

# tethered/untethered drop-down list
PLANNED = "PL"
UNPLANNED = "UP"
PLANNED_CHOICES = [
    (PLANNED, "Planned"),
    (UNPLANNED, "Unplanned"),
]


class Eva(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    code = models.IntegerField()
    astronaut = models.ForeignKey(
        "astronauts.Astronaut",
        on_delete=models.CASCADE,
        related_name="evas",
    )
    date = models.DateField(auto_now=False, auto_now_add=False)
    # mission =
    type = models.CharField(max_length=2, choices=TYPE_CHOICES)
    duration_secs = models.DurationField()
    tethered = models.CharField(max_length=2, choices=TETHERED_CHOICES, blank=True)
    planned = models.CharField(max_length=2, choices=PLANNED_CHOICES, default=PLANNED)
    notes = models.TextField(blank=True)
    image_photo = models.ImageField(
        upload_to="astronaut/photos",
        height_field=None,
        width_field=None,
        max_length=100,
        blank=True,
    )

    class Meta:
        ordering = ["date"]

    @property
    def get_full_astronaut_name(self):
        'Returns the astronauts full name - last, first "nickname".'
        return f"{self.astronaut.last_name}, {self.astronaut.first_name} {self.astronaut.nick_name}"

    def __str__(self):
        return self.astronaut.last_name

    def get_absolute_url(self):
        return reverse("eva_detail", args=[str(self.id)])
