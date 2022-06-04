from enum import Enum


class BlockchainNetwork(Enum):
    
    CELO = {
        "id": 0,
        "rpc_url": "https://example.com"
    }
    
    @classmethod
    def choices(cls):
        return ((i.name, i.value["id"]) for i in cls)


class ContractStatus(Enum):
    
    PENDING = 0
    
    ACTIVE = 1
    
    DISPUTE = 2
    
    COMPLETED = 3
    
    CANCELLED = 4
    
    @classmethod
    def choices(cls):
        return ((i.name, i.value) for i in cls)