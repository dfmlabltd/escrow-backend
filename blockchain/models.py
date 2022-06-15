import enum
from django.db import models
from contract.models import ContractModel
from . import enums
# Create your models here.


class TransactionModel(models.Model):

    transaction_hash = models.CharField(max_length=128)

    block_hash = models.CharField(max_length=128)

    contract = models.ForeignKey(ContractModel, on_delete=models.CASCADE)

    creator = models.CharField(max_length=64, blank=True)

    amount = models.IntegerField()

    description = models.CharField(max_length=64, null=True)

    status = models.IntegerField(choices=enums.TransactionStatus.choices(), 
                                 default=enums.TransactionStatus.PENDING.value)

    type = models.IntegerField(choices=enums.TransactionType.choices())

    identifier = models.IntegerField()
    
    class Meta:
        
        unique_together = ('identifier', 'type', 'contract')