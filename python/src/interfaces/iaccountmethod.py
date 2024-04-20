from abc import ABC, abstractmethod
from src.entities.person import Person

class IOperationMethod(ABC):
    @abstractmethod
    def do_transaction(self, sender: Person, recipient: Person, amount: float): pass
    
    @abstractmethod
    def validate_transaction(self, sender: Person, recipient: Person, amount: float): pass