# Generated by Django 4.2.6 on 2023-10-13 19:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0009_remove_log_server_response_and_more'),
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
