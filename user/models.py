from datetime import timedelta, datetime
from django.db import models
from django.conf import settings
from password_generator import PasswordGenerator

# Create your models here.

pwo = PasswordGenerator()
pwo.minlen = 64
pwo.maxlen = 128

def compute_expiry_time():
        
    return datetime.now() + timedelta(seconds=settings.EXPIRY_TIME)

def compute_otp():
    
    return pwo.generate()
    
class OTPModel(models.Model):
    
    code = models.CharField(max_length=128, default=compute_otp())
    
    expiry_time = models.DateTimeField(default=compute_expiry_time())
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    status = models.BooleanField(default=True)

    def is_valid(self):
        
        return self.status and (datetime.now > self.expiry_time) 