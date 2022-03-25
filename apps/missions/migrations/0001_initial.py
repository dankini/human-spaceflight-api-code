# Generated by Django 4.0.2 on 2022-03-22 21:28

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("agencies", "0003_allow_formed_date_blank_null"),
    ]

    operations = [
        migrations.CreateModel(
            name="Mission",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("name_aka", models.CharField(blank=True, max_length=50)),
                ("type", models.CharField(blank=True, max_length=255)),
                ("duration_secs", models.DurationField()),
                (
                    "distance_travelled_km",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=14, null=True
                    ),
                ),
                (
                    "distance_travelled_nmi",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=14, null=True
                    ),
                ),
                ("launch_date_time", models.DateTimeField()),
                (
                    "agency",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="agencies",
                        to="agencies.agency",
                    ),
                ),
            ],
            options={
                "ordering": ["launch_date_time"],
            },
        ),
    ]