# apps/agencies/admin.py

from django.contrib import admin
from apps.agencies.models import Agency


class AgencyAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "abbreviation",
        "country",
        "formed_date",
        "website",
    ]


admin.site.register(Agency, AgencyAdmin)
