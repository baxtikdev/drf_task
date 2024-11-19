from django.contrib.auth import get_user_model
from drf_spectacular.utils import extend_schema
from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenRefreshView

from api.auth.serializers import LogOutSerializer, UserLoginSerializer

User = get_user_model()


@extend_schema(tags=["Auth"])
class LoginAPIView(generics.CreateAPIView):
    serializer_class = UserLoginSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@extend_schema(tags=["Auth"])
class LogoutAPIView(generics.CreateAPIView):
    serializer_class = LogOutSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            token = RefreshToken(serializer.validated_data.get('refresh'))
            token.blacklist()
        except Exception as e:
            return Response({'message': "Token is invalid or blacklisting failed"}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message': "Successfully logged out"}, status=status.HTTP_200_OK)


@extend_schema(tags=["Auth"])
class TokenRefreshAPIView(TokenRefreshView):
    pass
