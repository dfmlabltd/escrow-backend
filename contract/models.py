from django.db import models
from . import enums
from django.contrib.auth import get_user_model

UserModel = get_user_model()

# Create your models here.



class ContractModel(models.Model):
    
    owner = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    
    agreement = models.URLField()
    
    amount = models.IntegerField()
    
    contract_address = models.CharField(max_length=64)
    
    token_address = models.CharField(max_length=64)
    
    blockchain_network =  models.IntegerField(choices=enums.BlockchainNetwork.choices())
    
    auto_withdraw = models.BooleanField(default=False)
    
    time_created = models.DateTimeField(auto_now_add=True)
    
    time_update = models.DateTimeField(auto_now=True)
    
    status = models.IntegerField(choices=enums.ContractStatus.choices(), default=enums.ContractStatus.PENDING.value)


class EntityModel(models.Model):
    
    amount = models.IntegerField()
    
    wallet_address = models.IntegerField()
    
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
        
    class Meta:
        
        abstract = True
        

class DepositorModel(EntityModel):
    
    contract = models.ForeignKey(ContractModel, on_delete=models.CASCADE, related_name="depositors")
    

class TrusteeModel(EntityModel):
    
    contract = models.ForeignKey(ContractModel, on_delete=models.CASCADE, related_name="trustees")