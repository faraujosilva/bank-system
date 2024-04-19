from abc import ABC, abstractmethod

class IAccountOperation(ABC):
    @abstractmethod
    def debit(self, amount: float): pass
    
    @abstractmethod
    def credit(self, amount: float): pass