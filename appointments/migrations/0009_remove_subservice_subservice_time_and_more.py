# Generated by Django 5.0.4 on 2024-05-01 10:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0008_alter_doctors_service_doctor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subservice',
            name='subservice_time',
        ),
        migrations.AddField(
            model_name='subservice',
            name='duration_minutes',
            field=models.DurationField(default=datetime.timedelta(seconds=1200)),
        ),
    ]
