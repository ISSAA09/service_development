from datetime import timedelta, time

from django.db import models

from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Client(models.Model):
    email = models.EmailField(max_length=100, verbose_name='контактный email')
    name = models.CharField(max_length=250, verbose_name='ФИО')
    comment = models.TextField(verbose_name='комментарий', **NULLABLE)

    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь', **NULLABLE)

    def __str__(self):
        return f'{self.name} ({self.email})'

    class Meta:
        verbose_name = 'клиент сервиса'
        verbose_name_plural = 'клиенты сервиса'


class MailingListSettings(models.Model):
    DAILY = timedelta(days=1)
    WEEKLY = timedelta(days=7)
    MONTHLY = timedelta(days=30, hours=12)

    PERIODICITY_CHOICES = [
        (DAILY, "Раз в день"),
        (WEEKLY, "Раз в неделю"),
        (MONTHLY, "Раз в месяц"),
    ]
    CREATED = 'Создана'
    STARTED = 'Запущена'
    COMPLETED = 'Завершена'

    STATUS_CHOICES = [
        (CREATED, "Создана"),
        (COMPLETED, "Завершена"),
        (STARTED, "Запущена"),
    ]
    TO_BE_SENT = 'К отправке'
    SHIPPED = 'Отправлено'

    STATUS_CHOICES_MESSAGE = [
        ('TO_BE_SENT', "К отправке"),
        ('SHIPPED', "Отправлено"),
    ]

    start_time = models.TimeField(verbose_name='время начала рассылки', default=time(hour=14))
    end_time = models.TimeField(verbose_name='время окончания рассылки', default=time(hour=15))
    periodicity = models.DurationField(verbose_name='периодичность', default=MONTHLY, choices=PERIODICITY_CHOICES)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default=CREATED, verbose_name='статус рассылки')

    clients = models.ManyToManyField(Client, verbose_name='клиенты рассылки')
    subject = models.CharField(max_length=250, verbose_name='тема письма')
    text = models.TextField(verbose_name='тело письма')
    status_message = models.CharField(max_length=50, choices=STATUS_CHOICES_MESSAGE, default=TO_BE_SENT,
                                      verbose_name='статус отправки')
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, **NULLABLE,
                              verbose_name='Пользователь')

    def __str__(self):
        return f'Время: {self.start_time} - {self.end_time}, Периодичность: {self.periodicity}, Статус: {self.status}'

    class Meta:
        verbose_name = 'настройка рассылки'
        verbose_name_plural = 'настройки рассылки'

        permissions = [
            ('change_status', 'Can turn off mailing')
        ]


class Log(models.Model):
    mailing_list = models.ForeignKey(MailingListSettings, on_delete=models.CASCADE, verbose_name='рассылка')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='клиент рассылки', **NULLABLE)

    time = models.DateTimeField(verbose_name='дата и время последней попытки', auto_now_add=True)
    status = models.BooleanField(verbose_name='статус попытки')

    def __str__(self):
        return f'{self.time} {self.status}'

    class Meta:
        verbose_name = 'лог'
        verbose_name_plural = 'логи'
