from rest_framework import serializers
from . import models

class TokenSerializer(serializers.ModelSerializer):
    
    class Meta:
        
        model = models.TokenModel
        
        fields = '__all__'
        
class BlockchainNetworkSerializer(serializers.ModelSerializer):
    
    class Meta:
        
        model = models.BlockchainNetworkModel
        
        fields = '__all__'