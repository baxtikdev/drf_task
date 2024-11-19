from drf_spectacular.utils import extend_schema
from rest_framework.filters import OrderingFilter
from rest_framework.viewsets import ModelViewSet

from api.booking.serializers import BookingCreateSerializer, BookingListSerializer
from api.filter import BookingFilter
from api.paginator import CustomPagination
from common.booking.models import Booking


@extend_schema(tags=["Booking"])
class BookingAPIView(ModelViewSet):
    queryset = Booking.objects.select_related('room', 'room__office', 'user').all()
    serializer_class = BookingCreateSerializer
    filter_backends = [BookingFilter, OrderingFilter]
    ordering_fields = ['id', 'name', 'capacity', 'user__first_name']
    pagination_class = CustomPagination
    lookup_field = 'guid'

    def list(self, request, *args, **kwargs):
        self.serializer_class = BookingListSerializer
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = BookingListSerializer
        return super().retrieve(request, *args, **kwargs)
