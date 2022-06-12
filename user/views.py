from rest_framework import generics

from . import models
from . import serializers
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from rest_framework import status
from . import throttles

UserModel = get_user_model()

class LoginView(generics.CreateAPIView):
    
    """
    Endpoint for login
    """
        
    throttle_classes = (throttles.LoginRateThrottle,)
    
    permission_classes = ()
    
    authentication_classes =  ()
    
    def create(self, request, *args, **kwargs):
        
        data = request.data
                
        email = data.get('email')
        
        try:

            validate_email(email)
            
        except ValidationError:
            
            return Response({ 'email': 'enter a valid email address' }, status=status.HTTP_401_UNAUTHORIZED)
        
        user, _ = UserModel.objects.get_or_create(email=email)
        
        models.OTPModel.create_otp(user)
        
        message = { 'email': email }
                        
        headers = self.get_success_headers(message)
        
        return Response(message, status=status.HTTP_202_ACCEPTED, headers=headers)


class ProfileView(generics.UpdateAPIView, generics.RetrieveAPIView):
    
    """
    Endpoint for retrieving and updating
    """
    
    serializer_class = serializers.ProfileSerializer

    def queryset(self):
        
        return self.request.user