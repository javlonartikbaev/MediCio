# Generated by Django 5.0.4 on 2024-05-01 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0004_appointment_service_id_doctors_service_doctor_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='service_id',
            field=models.ManyToManyField(to='appointments.subservice'),
        ),
    ]
