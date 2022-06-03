from rest_framework import generics

from . import models
from . import serializers
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework import status
from . import throttles



UserModel = get_user_model()

class LoginView(generics.CreateAPIView):
    
    """
    Endpoint for login
    """
    
    serializer_class = serializers.UserSerializer
    
    throttle_classes = (throttles.LoginRateThrottle,)
    
    permission_classes = ()
    
    authentication_classes =  ()
    
    def create(self, request, *args, **kwargs):
                                    
        serializer = self.get_serializer(data=request.data)
        
        serializer.is_valid()
        
        user, _ = UserModel.objects.get_or_create(email=request.data['email'])
        
        models.OTPModel.create_otp(user)
                
        headers = self.get_success_headers(serializer.data)
        
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED, headers=headers)


class UsernameView(generics.UpdateAPIView):
    
    """
    Endpoint for login
    """
    
    serializer_class = serializers.UsernameSerializer
