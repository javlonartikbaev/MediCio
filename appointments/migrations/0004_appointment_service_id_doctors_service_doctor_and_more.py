# Generated by Django 5.0.4 on 2024-05-01 04:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0003_alter_doctors_info_d'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='service_id',
            field=models.ManyToManyField(to='appointments.service'),
        ),
        migrations.AddField(
            model_name='doctors',
            name='service_doctor',
            field=models.ManyToManyField(to='appointments.subservice'),
        ),
        migrations.AddField(
            model_name='subservice',
            name='subservice_time',
            field=models.DateTimeField(default=datetime.datetime.utcnow),
        ),
        migrations.DeleteModel(
            name='AppointmentService',
        ),
    ]
