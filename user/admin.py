from django.conf import settings
from django.contrib import admin
from . import models

# Register your models here.

# if settings.DEBUG:
admin.site.register(models.OTPModel)
admin.site.register(models.PasswordlessUserModel)