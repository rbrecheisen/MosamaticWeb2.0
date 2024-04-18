from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Initialize users'

    def handle(self, *args, **kwargs):
        user = User.objects.filter(username='admin').first()
        if user is not None:
            user.delete()
        User.objects.create_superuser(
            username='admin', email='r.brecheisen@maastrichtuniversity.nl', password='Arturo4ever', first_name='Ralph', last_name='Brecheisen')
        user = User.objects.filter(username='stefan').first()
        if user is not None:
            user.delete()
        User.objects.create_user(username='stefan', email='stefan.bouwense@mumc.nl', password='Arturo4ever', first_name='Stefan', last_name='Bouwense')
        self.stdout.write(self.style.SUCCESS('Successfully initialized users'))
