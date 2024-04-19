from entities.person import Person
from src.interfaces.iaccountmethod import IOperationMethod

class CARD(IOperationMethod):
    def do_transaction(self, sender: Person, recipient: Person, amount: float):
        return super().do_transaction(sender, recipient, amount)
    
    def validate_transaction(self, sender: Person, recipient: Person, amount: float):
        return super().validate_transaction(sender, recipient, amount)