# Generated by Django 5.0.4 on 2024-05-05 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0013_alter_appointment_status_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='medical_insurance',
            field=models.CharField(default='', max_length=9, unique=True),
        ),
    ]