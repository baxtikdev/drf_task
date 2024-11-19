from django.urls import path

from api.auth.views import LogoutAPIView, LoginAPIView, TokenRefreshAPIView

urlpatterns = [
    path('login/', LoginAPIView.as_view(), name='login'),
    path('logout/', LogoutAPIView.as_view(), name="logout"),
    path('token/refresh/', TokenRefreshAPIView.as_view(), name='token_refresh')
]
