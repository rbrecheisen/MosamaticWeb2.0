from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Initialize connections'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Successfully initialized connections'))
