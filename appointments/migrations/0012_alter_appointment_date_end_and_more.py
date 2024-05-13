# Generated by Django 5.0.4 on 2024-05-03 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0011_remove_appointment_patient_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='date_end',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='date_of_birth',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='date_start',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='phone_number_p',
            field=models.CharField(max_length=13),
        ),
    ]