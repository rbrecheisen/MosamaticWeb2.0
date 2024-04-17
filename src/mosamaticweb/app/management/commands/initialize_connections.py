from django.core.management.base import BaseCommand

from ...models.connectionmodel import ConnectionModel


class Command(BaseCommand):
    help = 'Initialize connections'

    def handle(self, *args, **kwargs):
        connections = [
            ConnectionModel.objects.create(
                name='xnat-local',
                schema='http',
                hostname='localhost',
                port=80,
                username='admin',
                password='admin',
                project='test',
            )
        ]
        for connection in connections:
            self.stdout.write(self.style.SUCCESS(f' > Created connection {connection.name}'))
        self.stdout.write(self.style.SUCCESS('Successfully initialized connections'))