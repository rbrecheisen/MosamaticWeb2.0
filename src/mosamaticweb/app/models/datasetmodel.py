import uuid

from django.db import models
from django.conf import settings


class DatasetModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=1024, unique=True)
    owner = models.OneToOneField(settings.AUTH_USER_MODEL)
    origin = models.CharField(max_length=1024, unique=False)
    files = models.ManyToManyField('FileModel', related_name='dataset')