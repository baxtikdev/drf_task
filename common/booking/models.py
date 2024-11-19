from django.contrib.auth import get_user_model
from django.db import models

from common.base import BaseModel

User = get_user_model()


class Booking(BaseModel):
    room = models.ForeignKey('office.Room', related_name='roomBooking', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    user = models.ForeignKey(User, related_name='userBooking', on_delete=models.SET_NULL, null=True, blank=True)
