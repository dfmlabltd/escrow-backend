from rest_framework import serializers
from . import models

class DepositorSerializer(serializers.ModelSerializer):
    
    class Meta:
        
        model = models.DepositorModel
        
        fields = '__all__'
        

class TrusteeSerializer(serializers.ModelSerializer):
    
    class Meta:
        
        model = models.TrusteeModel
        
        fields = '__all__'


class ContractSerializer(serializers.ModelSerializer):
    
    depositors = DepositorSerializer(many=True)
    
    trustees = TrusteeSerializer(many=True)
    
    class Meta:
        
        model = models.ContractModel
        
        fields = '__all__'
    