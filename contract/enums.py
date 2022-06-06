from enum import Enum


class BlockchainNetwork(Enum):
    
    CELO = {
        "id": 0,
        "rpc_url": "https://example.com"
    }
    
    @classmethod
    def choices(cls):
        return ((i.value["id"], i.name) for i in cls)


class ContractStatus(Enum):
    
    PENDING = 0
    
    ACTIVE = 1
    
    DISPUTE = 2
    
    COMPLETED = 3
    
    CANCELLED = 4
    
    @classmethod
    def choices(cls):
        return ((i.value, i.name) for i in cls)