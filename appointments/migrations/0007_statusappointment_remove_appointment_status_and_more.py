# Generated by Django 5.0.4 on 2024-05-01 09:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0006_alter_subservice_subservice_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='StatusAppointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_name', models.CharField(max_length=55)),
            ],
            options={
                'verbose_name': 'Статус',
                'verbose_name_plural': 'Статусы',
                'db_table': 'status',
            },
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='status',
        ),
        migrations.AlterField(
            model_name='appointment',
            name='date_end',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='date_start',
            field=models.DateTimeField(),
        ),
        migrations.AlterModelTable(
            name='appointment',
            table='appointment',
        ),
        migrations.AddField(
            model_name='appointment',
            name='status_id',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='appointments.statusappointment'),
        ),
    ]
