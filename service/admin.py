from django.contrib import admin

from service.models import Client, MailingListSettings, Log


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['pk', 'email', 'name', ]
    list_filter = ['name', ]
    search_fields = ['email', 'name', 'comment', ]


@admin.register(MailingListSettings)
class MailingListSettingsAdmin(admin.ModelAdmin):
    list_display = ['pk', 'start_time', 'end_time', 'periodicity', 'status', ]
    list_filter = ['start_time', 'end_time', 'periodicity', 'status', ]
    search_fields = ['start_time', 'end_time', ]


@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
    list_display = ['pk', 'mailing_list', 'time', 'status', ]
    list_filter = ['mailing_list', 'status', ]
    search_fields = ['mailing_list', 'time', 'status', ]
