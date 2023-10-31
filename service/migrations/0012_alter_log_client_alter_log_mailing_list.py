# Generated by Django 4.2.6 on 2023-10-13 20:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0011_alter_log_client_alter_log_mailing_list'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='client',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='service.client', verbose_name='клиент рассылки'),
        ),
        migrations.AlterField(
            model_name='log',
            name='mailing_list',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.mailinglistsettings', verbose_name='рассылка'),
        ),
    ]
