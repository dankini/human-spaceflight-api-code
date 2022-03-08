# apps/astronauts/admin.py

from django.contrib import admin
from apps.astronauts.models import Astronaut


class AstronautAdmin(admin.ModelAdmin):
    list_display = [
        "last_name",
        "first_name",
        "nick_name",
        "nationality",
        "first_time_in_space_date",
        "total_duration_space_secs",
    ]


admin.site.register(Astronaut, AstronautAdmin)
