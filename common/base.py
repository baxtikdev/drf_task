import uuid
from django.db import models
from django.utils import timezone


class BaseModel(models.Model):
    guid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    registrationDate = models.DateTimeField(verbose_name="Дата регистрации", default=timezone.now)

    class Meta:
        abstract = True


class BaseMeta(object):
    ordering = ["-id"]
