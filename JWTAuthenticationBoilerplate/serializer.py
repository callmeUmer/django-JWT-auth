from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):

    groups = serializers.StringRelatedField(many=True)

    class Meta:
        model = User
        exclude = ['password', 'last_login', "user_permissions"]