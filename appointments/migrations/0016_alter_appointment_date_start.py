# Generated by Django 5.0.4 on 2024-05-07 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0015_remove_subservice_duration_minutes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='date_start',
            field=models.DateTimeField(null=True),
        ),
    ]
