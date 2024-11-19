from drf_spectacular.utils import extend_schema
from rest_framework.filters import OrderingFilter
from rest_framework.viewsets import ModelViewSet

from api.filter import LocationFilter, OfficeFilter, RoomFilter
from api.office.serializers import LocationCreateSerializer, OfficeCreateSerializer, OfficeListSerializer, \
    OfficeShortSerializer, RoomCreateSerializer, RoomListSerializer
from api.paginator import CustomPagination
from common.office.models import Location, Office, Room


@extend_schema(tags=["Location"])
class LocationAPIView(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationCreateSerializer
    filter_backends = [LocationFilter, OrderingFilter]
    ordering_fields = ['id', 'name']
    pagination_class = CustomPagination
    lookup_field = 'guid'


@extend_schema(tags=["Office"])
class OfficeAPIView(ModelViewSet):
    queryset = Office.objects.select_related('location').all()
    serializer_class = OfficeCreateSerializer
    filter_backends = [OfficeFilter, OrderingFilter]
    ordering_fields = ['id', 'name', 'location__name']
    pagination_class = CustomPagination
    lookup_field = 'guid'

    def list(self, request, *args, **kwargs):
        if request.query_params.get('short_search') == 'true':
            self.serializer_class = OfficeShortSerializer
        else:
            self.serializer_class = OfficeListSerializer
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = OfficeListSerializer
        return super().retrieve(request, *args, **kwargs)


@extend_schema(tags=["Room"])
class RoomAPIView(ModelViewSet):
    queryset = Room.objects.select_related('office', 'office__location').all()
    serializer_class = RoomCreateSerializer
    filter_backends = [RoomFilter, OrderingFilter]
    ordering_fields = ['id', 'name', 'capacity', 'user__first_name']
    pagination_class = CustomPagination
    lookup_field = 'guid'

    def list(self, request, *args, **kwargs):
        self.serializer_class = RoomListSerializer
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = RoomListSerializer
        return super().retrieve(request, *args, **kwargs)
