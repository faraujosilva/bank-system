from src.entities.person import Person
from src.utils.general import AccountInfo, AccountErrors

from src.interfaces.iaccountoperation import IAccountOperation

class AccountOperations:
    def __init__(self, person: Person, operations: IAccountOperation):
        self.person = person
        self.operations = operations

    def update_balance(self, amount: float):
        client_balance = self.person.account.get_balance()
        special_balance = self.person.account.get_special_credit()
        
        if amount > 0: # + 300
            self.operations.credit(amount)
            return AccountInfo.SUCCESS_CREDIT
        
        if client_balance < 0: #special credit
            if (amount * -1) > ((client_balance*-1) + (special_balance)):
                raise AccountErrors.NO_ENOUGH_LIMIT.value
            
            if client_balance + (special_balance*-1) > client_balance + amount:
                raise AccountErrors.NO_ENOUGH_LIMIT.value

            self.operations.debit(amount)
            return AccountInfo.SUCCESS_DEBIT
        
        if (client_balance - (amount*-1)) < 0:
            raise AccountErrors.NO_ENOUGH_MONEY.value        
            
        else:
            self.operations.debit(amount)
            return AccountInfo.SUCCESS_DEBIT
