from django.core.management import BaseCommand
from service.utils import send_mails


class Command(BaseCommand):
    def handle(self, *args, **options):
        send_mails()
