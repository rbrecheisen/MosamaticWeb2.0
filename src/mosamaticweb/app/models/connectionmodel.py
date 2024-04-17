import uuid

from django.db import models


class ConnectionModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=1024, unique=True)
    schema = models.CharField(max_length=5)
    hostname = models.CharField(max_length=512)
    port = models.IntegerField(max_length=5, editable=True)
    username = models.CharField(max_length=512, editable=True)
    password = models.CharField(max_length=512, editable=True)
    project = models.CharField(max_length=1024, editable=True, null=True)