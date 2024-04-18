import uuid

from django.db import models


class FileModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=1024, unique=False)
    path = models.CharField(max_length=1024, unique=False)
    dataset = models.ForeignKey('DatasetModel', on_delete=models.CASCADE, related_name='files')