# Generated by Django 4.0.2 on 2022-03-27 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('missions', '0005_rename_field_to_crew_members'),
    ]

    operations = [
        migrations.RenameField(
            model_name='crew',
            old_name='crew_member',
            new_name='astronaut',
        ),
        migrations.RemoveField(
            model_name='crew',
            name='mission_age',
        ),
        migrations.AddField(
            model_name='crew',
            name='mission_age_days',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='crew',
            name='mission_age_months',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='crew',
            name='mission_age_years',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
