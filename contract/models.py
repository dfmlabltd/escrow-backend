from uuid import uuid4
from django.db import models
from . import enums
from django.contrib.auth import get_user_model
from coin.models import TokenModel
UserModel = get_user_model()

# Create your models here.


def generate_UUID():
    # TO DO
    # fetch UUID from blockchain
    
    return uuid4

class ContractModel(models.Model):
    
    id = models.UUIDField(primary_key=True, default=generate_UUID, editable=False)
    
    title = models.CharField(max_length=128)
    
    owner = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    
    agreement = models.URLField(blank=True)
    
    amount = models.IntegerField()
    
    contract_address = models.CharField(max_length=64, blank=True, null=True)
    
    token = models.ForeignKey(TokenModel, on_delete=models.CASCADE)
        
    auto_withdraw = models.BooleanField(default=False)
    
    time_created = models.DateTimeField(auto_now_add=True)
    
    time_update = models.DateTimeField(auto_now=True)
    
    status = models.IntegerField(choices=enums.ContractStatus.choices(), default=enums.ContractStatus.PENDING.value)

    dispute_wait_day = models.IntegerField(default=1)

class EntityModel(models.Model):
    
    amount = models.IntegerField()
    
    wallet_address = models.CharField(max_length=64)
    
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
        
    class Meta:
        
        unique_together = ('user', 'contract')
        
        abstract = True
        

class DepositorModel(EntityModel):
    
    contract = models.ForeignKey(ContractModel, on_delete=models.CASCADE, related_name="depositors")
    

class TrusteeModel(EntityModel):
    
    contract = models.ForeignKey(ContractModel, on_delete=models.CASCADE, related_name="trustees")