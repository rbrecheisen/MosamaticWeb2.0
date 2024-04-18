from django.core.management.base import BaseCommand

from ...models.taskmodel import TaskModel


class Command(BaseCommand):
    help = 'Initialize tasks'

    def handle(self, *args, **kwargs):
        tasks = [
            TaskModel.objects.create(
                name='dummy',
                parameters=[
                    {
                        'name': 'model_files',
                        'display_name': 'AI model files',
                        'data_type': 'dataset',
                        'required': True,
                    },
                    {
                        'name': 'l3_images',
                        'display_name': 'L3 images',
                        'data_type': 'dataset',
                        'required': True
                    },
                ]
            )
        ]
        for task in tasks:
            self.stdout.write(self.style.SUCCESS(f' > Created task {task.name}'))
        self.stdout.write(self.style.SUCCESS('Successfully initialized tasks'))
