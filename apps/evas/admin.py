# apps/evas/admin.py

from django.contrib import admin
from apps.evas.models import Eva


class EvaAdmin(admin.ModelAdmin):
    list_display = [
        "code",
        "astronaut",
        "date",
        "type",
        "duration_secs",
        "notes",
    ]


admin.site.register(Eva, EvaAdmin)
