from django.conf import settings
from django.contrib.auth.backends import ModelBackend
from .models import OTPModel
from django.contrib.auth import get_user_model


UserModel = get_user_model()


class PasswordlessBackend(ModelBackend):

    def authenticate(self, request, **kwargs) -> UserModel:

        email = kwargs.get(settings.USERNAME_FIELD)

        code = kwargs.get('password')

        if email is None or code is None:

            return

        try:

            user = UserModel._default_manager.get_by_natural_key(
                email)

        except UserModel.DoesNotExist:

            return

        if not self.user_can_authenticate(user):

            return

        try:

            otp = OTPModel.objects.get(user=user, code=code)

            if otp.is_valid():

                OTPModel.invalidate_otp(otp)

                return user

        except OTPModel.DoesNotExist:

            return