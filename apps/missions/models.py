# apps/missions/models.py

import uuid
from django.db import models
from django.urls import reverse


class Mission(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    name = models.CharField(max_length=50)
    name_aka = models.CharField(max_length=50, blank=True)
    type = models.CharField(max_length=255, blank=True)
    agency = models.ForeignKey(
        "agencies.Agency",
        on_delete=models.CASCADE,
        related_name="agencies",
    )
    duration_secs = models.DurationField()
    distance_travelled_km = models.DecimalField(
        max_digits=14, decimal_places=2, null=True, blank=True
    )
    distance_travelled_nmi = models.DecimalField(
        max_digits=14, decimal_places=2, null=True, blank=True
    )
    launch_date_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    crew_size = models.IntegerField(null=True, blank=True)
    crew_members = models.ManyToManyField("astronauts.Astronaut")
    image_mission_patch = models.ImageField(
        upload_to="mission/patch",
        height_field=None,
        width_field=None,
        max_length=100,
        blank=True,
    )

    class Meta:
        ordering = ["launch_date_time"]

    @property
    def get_full_astronaut_name(self):
        'Returns the astronauts full name - last, first "nickname".'
        return f"{self.astronaut.last_name}, {self.astronaut.first_name} {self.astronaut.nick_name}"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("mission_detail", args=[str(self.id)])


"""
class Crew(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    name = models.ForeignKey(
        "astronauts.Astronaut",
        on_delete=models.CASCADE,
    )
    mission = models.ForeignKey(
        "Mission",
        on_delete=models.CASCADE,
    )
    role = models.CharField(max_length=50, blank=True)
    mission_age = models.DurationField()

    class Meta:
        db_table = "missions_mission_crew_members"
"""
"""
    @property
    def get_full_astronaut_name(self):
        'Returns the astronauts full name - last, first "nickname".'
        return f"{self.astronaut.last_name}, {self.astronaut.first_name} {self.astronaut.nick_name}"

    def __str__(self):
        return self.name.last_name

    def get_absolute_url(self):
    return reverse("crew_detail", args=[str(self.id)])
"""
