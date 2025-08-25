# apps/missions/models.py

import uuid
from django.db import models
from django.urls import reverse
from apps.astronauts.models import Astronaut  # Import Astronaut model
from dateutil.relativedelta import relativedelta # Import relativedelta for age calculations

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
        related_name="missions",
    )
    duration_secs = models.DurationField()
    distance_travelled_km = models.DecimalField(
        max_digits=14, decimal_places=2, null=True, blank=True
    )
    distance_travelled_nmi = models.DecimalField(
        max_digits=14, decimal_places=2, null=True, blank=True
    )
    launch_date_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    crew_members = models.ManyToManyField("astronauts.Astronaut", through="Crew")
    image_mission_patch = models.ImageField(
        upload_to="mission/patch",
        max_length=100,
        blank=True,
    )

    class Meta:
        ordering = ["launch_date_time"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("mission_detail", args=[str(self.id)])

    @property
    def crew_size(self):
        """Dynamically count crew members."""
        return self.crew_members.count()

    @property
    def get_crew_names(self):
        """Returns a list of astronaut names for this mission."""
        return ", ".join(self.crew_members.values_list("first_name", "last_name", flat=False))


class Crew(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    astronaut = models.ForeignKey(
        "astronauts.Astronaut",
        on_delete=models.CASCADE,
    )
    mission = models.ForeignKey(
        "Mission",
        on_delete=models.CASCADE,
    )
    role = models.CharField(max_length=50, blank=True)
    # mission_age_years = models.IntegerField(null=True, blank=True)
    # mission_age_months = models.IntegerField(null=True, blank=True)
    # mission_age_days = models.IntegerField(null=True, blank=True)


    class Meta:
        ordering = ["mission"]

    #def __str__(self):
        #return f"{self.astronaut.first_name} {self.astronaut.last_name} - {self.role}"
    
    def __str__(self):
        return self.astronaut.get_full_astronaut_name  # Uses mixin from Astronaut to display full astronaut name

    
    def get_absolute_url(self):
        """Redirect 'View on site' to the astronaut's profile instead of crew detail."""
        return reverse("astronaut_detail", args=[str(self.astronaut.id)])

    
    @property
    def age_at_launch_ymd(self):
        """Calculate astronaut's exact age at the time of launch in years, months, and days."""
        if not self.astronaut.birth_date or not self.mission.launch_date_time:
            return "Unknown"  # Avoid errors if data is missing
        
        birth_date = self.astronaut.birth_date
        launch_date = self.mission.launch_date_time.date()  # Extract date part

        age = relativedelta(launch_date, birth_date)
        return f"{age.years} years, {age.months} months, {age.days} days"
