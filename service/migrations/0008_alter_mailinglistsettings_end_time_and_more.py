# Generated by Django 4.2.6 on 2023-10-12 09:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0007_alter_mailinglistsettings_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailinglistsettings',
            name='end_time',
            field=models.TimeField(default=datetime.time(15, 0), verbose_name='время окончания рассылки'),
        ),
        migrations.AlterField(
            model_name='mailinglistsettings',
            name='start_time',
            field=models.TimeField(default=datetime.time(14, 0), verbose_name='время начала рассылки'),
        ),
    ]
