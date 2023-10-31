# Generated by Django 4.2.6 on 2023-10-12 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0006_remove_mailinglistsettings_clients_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailinglistsettings',
            name='status',
            field=models.CharField(choices=[('Создана', 'Создана'), ('Завершена', 'Завершена'), ('Запущена', 'Запущена')], default='Создана', max_length=50, verbose_name='статус рассылки'),
        ),
    ]