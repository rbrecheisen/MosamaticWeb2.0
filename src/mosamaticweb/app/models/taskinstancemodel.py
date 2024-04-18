import uuid

from django.db import models


class TaskInstanceModel(models.Model):
    STATUS_CHOICES = [
        ('IDLE', 'Idle'),
        ('RUNNING', 'Running'),
        ('CANCELED', 'Canceled'),
        ('ERROR', 'Error'),
        ('FINISHED', 'Finished'),
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    task_id = models.CharField(max_length=32)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    parameter_values = models.JSONField()