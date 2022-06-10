from rest_framework import generics
from . import serializers
from . import models
# Create your views here.


class BlockchainNetworkView(generics.ListAPIView):

    serializer_class = serializers.BlockchainNetworkSerializer

    queryset = models.BlockchainNetworkModel.objects.all()


class TokenView(generics.ListAPIView):

    serializer_class = serializers.TokenSerializer

    queryset = models.TokenModel.objects.all()

    def get_queryset(self):
        return super().get_queryset().filter(
            network__id=self.kwargs['pk']
        )
