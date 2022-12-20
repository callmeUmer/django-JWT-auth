from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializer import UserSerializer

class UserObjectPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        # injecting the user obj
        data['user'] = UserSerializer(self.user).data

        return data




class UserObjectPairView(TokenObtainPairView):
    serializer_class = UserObjectPairSerializer