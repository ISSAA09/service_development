# Generated by Django 4.2.6 on 2023-10-11 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0004_alter_mailinglistsettings_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailinglistsettings',
            name='status',
            field=models.CharField(choices=[('Создана', 'Завершена'), ('Завершена', 'Создана'), ('Запущена', 'Запущена')], default='Создана', max_length=50, verbose_name='статус рассылки'),
        ),
    ]
