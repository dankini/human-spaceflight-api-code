# apps/astronauts/admin.py

# deviates from standard admin.py layout so that we can incorporate data import/export functionality in admin interface using django-import-export library

from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from apps.astronauts.models import Astronaut


# class AstronautAdmin(admin.ModelAdmin):
@admin.register(Astronaut)
class AstronautAdmin(ImportExportModelAdmin):
    list_display = [
        "last_name",
        "first_name",
        "nick_name",
        "nationality",
        "first_time_in_space_date",
        "total_duration_space_secs",
    ]
    search_fields = ('first_name', 'last_name')
