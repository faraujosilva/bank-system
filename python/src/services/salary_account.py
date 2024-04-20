from src.interfaces.iaccountoperation import IAccountOperation
from src.interfaces.iaccountmethod import IOperationMethod
from src.entities.person import Person

class SalaryAccountOperation(IAccountOperation):
    def __init__(self, sender: Person, recipient: Person, method: IOperationMethod):
        self.sender = sender
        self.recipient = recipient
        self.method = method
        
    def debit(self, amount: float):
        return self.method.do_transaction(self.sender, self.recipient, amount)
    
    def credit(self, amount: float):
        return self.method.do_transaction(self.sender, self.recipient, amount)