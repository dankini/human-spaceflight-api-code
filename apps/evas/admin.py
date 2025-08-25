# apps/evas/admin.py

# deviates from standard admin.py layout so that we can incorporate data import/export functionality in admin interface using django-import-export library

from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from apps.evas.models import Eva


# class EvaAdmin(admin.ModelAdmin):
@admin.register(Eva)
class EvaAdmin(ImportExportModelAdmin):
    list_display = [
        "code",
        "astronaut",
        "date",
        "type",
        "duration_secs",
        "notes",
    ]
