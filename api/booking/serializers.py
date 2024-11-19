from django.contrib.auth import get_user_model
from django.utils.timezone import make_aware
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from api.office.serializers import RoomShortSerializer
from common.booking.models import Booking

User = get_user_model()


class UserShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'guid', 'username', 'first_name', 'last_name', 'birthday']


class BookingCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'guid', 'room', 'name', 'start_time', 'end_time', 'user']

    def validate(self, attrs):
        room = attrs.get('room')
        start_time = attrs.get('start_time')
        end_time = attrs.get('end_time')

        start_time = make_aware(start_time) if not start_time.tzinfo else start_time
        end_time = make_aware(end_time) if not end_time.tzinfo else end_time

        if start_time >= end_time:
            raise ValidationError("Start time must be before end time.")

        overlapping_bookings = Booking.objects.filter(
            room=room,
            start_time__lt=end_time,
            end_time__gt=start_time
        )

        if overlapping_bookings.exists():
            raise ValidationError("This room is already booked for the requested time.")

        return attrs


class BookingListSerializer(serializers.ModelSerializer):
    room = RoomShortSerializer()
    user = UserShortSerializer()

    class Meta:
        model = Booking
        fields = ['id', 'guid', 'room', 'name', 'start_time', 'end_time', 'user']
