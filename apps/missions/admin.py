# apps/missions/admin.py

# deviates from standard admin.py layout so that we can incorporate data import/export functionality in admin interface using django-import-export library

from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from apps.missions.models import Mission


# class MissionAdmin(admin.ModelAdmin):
@admin.register(Mission)
class MissionAdmin(ImportExportModelAdmin):
    list_display = [
        "name",
        "agency",
        "launch_date_time",
        "duration_secs",
    ]


# admin.site.register(Mission, MissionAdmin)

"""
@admin.register(Crew)
class CrewAdmin(ImportExportModelAdmin):
    list_display = [
        "name",
        "mission",
        "role",
        "mission_age",
    ]


# admin.site.register(Crew, CrewAdmin)
"""
