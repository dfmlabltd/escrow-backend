from rest_framework import viewsets, generics, mixins
from django.db.models import Q
from rest_framework.response import Response
from . import models
from . import serializers
from rest_framework import status
from escrow.permissions import IsActive
from . import permissions


class ContractView(viewsets.ViewSet, generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.ListModelMixin, mixins.CreateModelMixin):

    queryset = models.ContractModel.objects.all()

    serializer_class = serializers.ContractSerializer

    permission_classes = (IsActive, permissions.ContractReadOnlyPermission, )

    def create(self, request, *args, **kwargs):

        current_user: models.UserModel = request.user

        data = request.data

        data["owner"] = current_user.id

        serializer = self.get_serializer(data=data)

        serializer.is_valid(raise_exception=True)

        self.perform_create(serializer)

        headers = self.get_success_headers(serializer.data)

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
