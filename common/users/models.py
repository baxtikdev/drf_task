from django.contrib.auth.models import AbstractUser
from django.db import models

from common.base import BaseModel
from common.users.manager import UserManager


class User(AbstractUser, BaseModel):
    surname = models.CharField(max_length=100, null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)

    objects = UserManager()

    def __str__(self):
        return self.first_name + ' ' + str(self.last_name)
