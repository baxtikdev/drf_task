from rest_framework import serializers

from common.office.models import Location, Office, Room


class LocationCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'guid', 'name']


class OfficeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Office
        fields = ['id', 'guid', 'location', 'name']


class OfficeShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Office
        fields = ['id', 'guid', 'name']


class OfficeListSerializer(serializers.ModelSerializer):
    location = LocationCreateSerializer()

    class Meta:
        model = Office
        fields = ['id', 'guid', 'location', 'name']


class RoomCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id', 'guid', 'office', 'name', 'capacity']


class RoomShortSerializer(serializers.ModelSerializer):
    office = OfficeShortSerializer()

    class Meta:
        model = Room
        fields = ['id', 'guid', 'office', 'name', 'capacity']


class RoomListSerializer(serializers.ModelSerializer):
    office = OfficeListSerializer()

    class Meta:
        model = Room
        fields = ['id', 'guid', 'office', 'name', 'capacity']
