from rest_framework import serializers
from django.contrib.auth import get_user_model
from . import models

UserModel = get_user_model()

class UserSerializer(serializers.ModelSerializer):

    class Meta:

        model = UserModel

        fields = ('email', )

class UsernameSerializer(serializers.ModelSerializer):

    class Meta:

        model = UserModel

        fields = ('username', )


class OTPSerializer(serializers.ModelSerializer):

    class Meta:

        model = models.OTPModel

        fields = ('user', 'code', )
