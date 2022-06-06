from rest_framework import viewsets, generics, mixins
from rest_framework.response import Response
from rest_framework import filters
from django.db.models import Q
from . import pagination
from . import models
from . import serializers
from rest_framework import status

class ContractView(viewsets.ViewSet, generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.ListModelMixin, mixins.CreateModelMixin):

    serializer_class = serializers.ContractSerializer
    
    pagination_class = pagination.ContractPagination
    
    filter_backends = [filters.SearchFilter]
    
    search_fields = ('$title', '$amount', '$contract_address')
    
    def get_queryset(self):
        
        current_user: models.UserModel = self.request.user
        
        contracts = models.ContractModel.objects.select_related().filter(
            Q(owner=current_user) |
            Q(depositors__user=current_user) |
            Q(trustees__user=current_user)
        )

        return contracts

    def create(self, request, *args, **kwargs):

        current_user: models.UserModel = request.user

        data = request.data

        data["owner"] = current_user.id

        serializer = self.get_serializer(data=data)

        serializer.is_valid(raise_exception=True)

        self.perform_create(serializer)

        headers = self.get_success_headers(serializer.data)

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

