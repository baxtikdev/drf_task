from django.db import models

from common.base import BaseModel


class Location(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Office(BaseModel):
    location = models.ForeignKey(Location, related_name='locationOffice', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Room(BaseModel):
    office = models.ForeignKey(Office, related_name='officeRoom', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    capacity = models.PositiveIntegerField()

    def __str__(self):
        return self.name
