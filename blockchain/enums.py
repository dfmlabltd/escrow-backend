from enum import Enum


class TransactionStatus(Enum):
    
    PENDING = 0
    
    ACCEPTED = 1
    
    REJECTED = 2
    
    COMPLETED = 3

    @classmethod
    def choices(cls):
        return ((i.value, i.name) for i in cls)
    
    
class TransactionType(Enum):
    
    WITHDRAWAL = 0
    
    DEPOSIT = 1

    @classmethod
    def choices(cls):
        return ((i.value, i.name) for i in cls)