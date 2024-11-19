from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()


class LogOutSerializer(serializers.Serializer):
    refresh = serializers.CharField(write_only=True, max_length=255, required=True)


class UserLoginSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    guid = serializers.CharField(read_only=True)
    role = serializers.CharField(read_only=True)
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128, write_only=True)
    access = serializers.CharField(read_only=True)
    refresh = serializers.CharField(read_only=True)

    def validate(self, data):
        username = data['username']
        password = data['password']

        user = authenticate(username=username, password=password)

        if user is None:
            raise serializers.ValidationError("User does not exist")
        try:
            refresh = RefreshToken.for_user(user)
            validation = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'id': user.id,
                'guid': user.guid,
                'username': user.username,
                'role': user.role
            }
            return validation
        except User.DoesNotExist:
            raise serializers.ValidationError("User does not exist")

    class Meta:
        model = User
        fields = ('id', 'guid', 'role', 'username', 'password', 'access', 'refresh')
        read_only_fields = ('id', 'role', 'isInpatient', 'access', 'refresh')
