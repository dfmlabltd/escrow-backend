from __future__ import annotations
from datetime import timedelta
from django.utils import timezone
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from password_generator import PasswordGenerator
from user.fields import UsernameField
from user.validators import validate_username
# Create your models here.

class PasswordlessUserModel(AbstractUser):
        
    first_name = None
    
    last_name = None
    
    username = UsernameField(max_length=16, validators=(validate_username,), null=True, blank=True)
    
    email = models.EmailField(unique=True, max_length=128)
        
    USERNAME_FIELD = settings.USERNAME_FIELD
    
    REQUIRED_FIELDS = ['username']
    

def compute_expiry_time() -> timezone:

    return timezone.now() + timedelta(seconds=settings.OTP_EXPIRY_TIME)


def compute_otp() -> str:

    pwo = PasswordGenerator()
    
    pwo.minlen = 64
    
    pwo.maxlen = 128

    return pwo.generate()


class OTPModel(models.Model):

    code = models.CharField(max_length=128, default=compute_otp())

    expiry_time = models.DateTimeField(default=compute_expiry_time())

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)

    status = models.BooleanField(default=True)

    def is_valid(self) -> bool:

        return self.status and (self.expiry_time > timezone.now())

    @classmethod
    def invalidate_otp(cls: OTPModel, otp: OTPModel) -> OTPModel:

        otp.status = False

        otp.save()

        return otp

    @classmethod
    def create_otp(cls: OTPModel, user: settings.AUTH_USER_MODEL) -> OTPModel:
        
        cls.invalidate_user_otps(user)

        otp = cls(user=user)

        otp.save()

        return otp

    @classmethod
    def invalidate_user_otps(cls: OTPModel, user: settings.AUTH_USER_MODEL) -> settings.AUTH_USER_MODEL:
        
        otps = cls.objects.filter(user=user, status=True)
        
        otps.update(status=False)