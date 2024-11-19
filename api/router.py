from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from api.booking.views import BookingAPIView
from api.office.views import LocationAPIView, OfficeAPIView, RoomAPIView

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register(r"location", LocationAPIView)
router.register(r"office", OfficeAPIView)
router.register(r"room", RoomAPIView)
router.register(r"booking", BookingAPIView)

urlpatterns = router.urls
