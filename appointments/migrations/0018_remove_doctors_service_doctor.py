# Generated by Django 5.0.4 on 2024-05-10 04:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0017_alter_appointment_phone_number_p'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctors',
            name='service_doctor',
        ),
    ]
