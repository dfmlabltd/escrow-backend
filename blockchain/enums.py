from enum import Enum


class TransactionStatus(Enum):
    
    PENDING = 0
    
    APPROVED = 1
    
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
    
class EventType(Enum):

    DEPOSIT = 0

    REQUEST = 1

    REJECTED = 2

    VOTE = 3

    APPROVED = 4

    WITHDRAW = 5