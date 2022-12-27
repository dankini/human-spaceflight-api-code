# apps/astronauts/models.py
import uuid
from django.db import models
from django.urls import reverse


class Astronaut(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True)
    nick_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField(auto_now=False, auto_now_add=False)
    birth_town_city = models.CharField(max_length=50, blank=True)
    birth_state = models.CharField(max_length=50, blank=True)
    birth_country = models.CharField(max_length=50, blank=True)
    death_date = models.DateField(
        auto_now=False, auto_now_add=False, null=True, blank=True
    )
    resting_place = models.CharField(max_length=50, blank=True)
    # alma_mater_list = models.ForeignKey(AlmaMater, on_delete=models.CASCADE)
    # occupation_list = models.ForeignKey(Occupation, on_delete=models.CASCADE)
    rank_attained = models.CharField(max_length=100)
    service_branch = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
    first_time_in_space_date = models.DateField(auto_now=False, auto_now_add=False)
    total_duration_space_secs = models.DurationField()
    # calculable - sum(duration(missions(astronaut))
    # mission_list = models.ForeignKey(Mission, on_delete=models.CASCADE)
    # mission_insignia_list = models.ForeignKey(Insignia, on_delete=models.CASCADE)
    # selection_group = models.ForeignKey(SelectionGroup, on_delete=models.CASCADE)
    # eva_model total_eva =
    # eva_model total_eva_duration_space_secs =
    # total lunar surface time =
    # award_list = models.ForeignKey(Award, on_delete=models.CASCADE)
    retirement_date = models.DateField(
        auto_now=False, auto_now_add=False, null=True, blank=True
    )
    image_photo = models.ImageField(
        upload_to="astronaut/photos",
        height_field=None,
        width_field=None,
        max_length=100,
        blank=True,
    )
    image_signature = models.ImageField(
        upload_to="astronaut/signatures",
        height_field=None,
        width_field=None,
        max_length=100,
        blank=True,
    )
    wikipedia_bio_website = models.URLField(max_length=100, blank=True)

    class Meta:
        ordering = ["first_time_in_space_date"]

    @property
    def get_full_astronaut_name(self):
        'Returns the astronauts full name in format - last_name, first_name "nick_name".'
        return f"{self.last_name}, {self.first_name} {self.nick_name}"

    def __str__(self):
        return self.last_name

    def get_absolute_url(self):
        return reverse("astronaut_detail", args=[str(self.id)])
