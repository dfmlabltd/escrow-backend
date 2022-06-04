from ast import Return
from rest_framework import viewsets, generics
from django.db.models import Q
from rest_framework.response import Response
from . import models
from . import serializers
from rest_framework import status


class ContractView(viewsets.ViewSet, generics.GenericAPIView):
    
    serializer_class = serializers.ContractSerializer
    
    def create(self, request, *args, **kwargs):
        
        current_user : models.UserModel = request.user
        
        data = request.data
        
        data["owner"] = current_user.id
        
        serializer = self.get_serializer(data=data)
        
        serializer.is_valid(raise_exception=True)
        
        self.perform_create(serializer)
        
        headers = self.get_success_headers(serializer.data)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def list(self, request):

        current_user: models.UserModel = request.user

        """
        complex query!
        this query uses reversed foreignkey to get the contracts 
        connected to the current logged in user
        it retrieves all related names and perform a filter
        """
        
        contracts = models.ContractModel.objects.select_related().filter(
            Q(user=current_user) |
            Q(depositors_user=current_user) |
            Q(trustees_user=current_user)
        )

        serializer = self.get_serializer(contracts, many=True)
        
        return Response(serializer.data)
