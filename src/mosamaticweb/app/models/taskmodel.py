import uuid

from django.db import models


class TaskModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=1024, unique=False)
    parameters = models.JSONField()