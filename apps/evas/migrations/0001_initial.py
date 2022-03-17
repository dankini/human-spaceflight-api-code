# Generated by Django 4.0.2 on 2022-03-10 16:01

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('astronauts', '0002_allow_blank_null_for_datetime_fields'),
    ]

    operations = [
        migrations.CreateModel(
            name='Eva',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('type', models.CharField(choices=[('SU', 'Stand-up'), ('SW', 'Spacewalk'), ('MW', 'Moonwalk')], max_length=2)),
                ('duration_secs', models.DurationField()),
                ('tethered', models.CharField(blank=True, choices=[('TE', 'Tethered'), ('UT', 'Untethered')], max_length=2)),
                ('planned', models.CharField(choices=[('PL', 'Planned'), ('UP', 'Unplanned')], default='PL', max_length=2)),
                ('notes', models.TextField(blank=True)),
                ('image_photo', models.ImageField(blank=True, upload_to='astronaut/photos')),
                ('astronaut', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='astronauts.astronaut')),
            ],
            options={
                'ordering': ['date'],
            },
        ),
    ]