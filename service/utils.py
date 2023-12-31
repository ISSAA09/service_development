from datetime import datetime

from django.core.cache import cache
from django.core.mail import send_mail
from django.conf import settings
import django.utils.timezone

from service.models import MailingListSettings, Log


def _send_email(client, mailing, message):
    result = send_mail(
        subject=message.subject,
        message=message.text,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[client.email],
        fail_silently=False,
    )

    Log.objects.create(
        mailing_list=mailing,
        client=client,
        status=result,
    )


def send_mails():
    now = datetime.now()
    now_time = now.time()

    for mailing in MailingListSettings.objects.filter(status=MailingListSettings.STARTED):

        if mailing.start_time < now_time < mailing.end_time:

            for mailing_client in mailing.clients.all():
                message = mailing
                log = Log.objects.filter(
                    client=mailing_client,
                    mailing_list=mailing
                )
                if log.exists():
                    last_try_date = log.order_by('-time').first().time.replace(tzinfo=None)
                    if mailing.periodicity == MailingListSettings.DAILY:
                        if (now - last_try_date) >= MailingListSettings.DAILY:
                            _send_email(mailing_client, mailing, message)

                    elif mailing.periodicity == MailingListSettings.WEEKLY:
                        if (now - last_try_date) >= MailingListSettings.WEEKLY:
                            _send_email(mailing_client, mailing, message)

                    elif mailing.periodicity == MailingListSettings.MONTHLY:
                        if (now - last_try_date) >= MailingListSettings.MONTHLY:
                            _send_email(mailing_client, mailing, message)

                else:
                    _send_email(mailing_client, mailing, message)

            message.status = MailingListSettings.SHIPPED
            message.save()


class MailingListCacheMixin:

    def get_mailing_list_cache(self):
        if settings.CACHE_ENABLED:
            key = 'mailing_list'
            queryset = cache.get(key)

            if queryset is None:
                queryset = super().get_queryset()
                cache.set(key, queryset)

        else:
            queryset = super().get_queryset()

        return queryset
