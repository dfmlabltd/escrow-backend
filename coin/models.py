from django.db import models

# Create your models here.

class BlockchainNetworkModel(models.Model):
    
    name = models.CharField(max_length=64)
    
    rpc = models.URLField()
    
    chain = models.IntegerField()
    
    explorer = models.URLField()
    

class TokenModel(models.Model):
    
    name = models.CharField(max_length=32)
    
    contract = models.CharField(max_length=64)
    
    symbol = models.CharField(max_length=8)
    
    decimal = models.IntegerField()
    
    network = models.ForeignKey(BlockchainNetworkModel, on_delete=models.CASCADE)