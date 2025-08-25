# apps/agencies/admin.py

# deviates from standard admin.py layout so that we can incorporate data import/export functionality in admin interface using django-import-export library

from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from apps.agencies.models import Agency


# class AgencyAdmin(admin.ModelAdmin):
@admin.register(Agency)
class AgencytAdmin(ImportExportModelAdmin):
    list_display = [
        "name",
        "abbreviation",
        "country",
        "formed_date",
        "website",
    ]
