from src.entities.person import Person
from src.interfaces.iaccountmethod import IOperationMethod
from src.utils.general import PIXInfo

class PIX(IOperationMethod):
    def do_transaction(self, sender: Person, recipient: Person, amount: float):
        print(PIXInfo.START_PIX.value)

        try:
            if self.validate_transaction(sender, recipient, amount):
                sender.account.update_balance(amount)
                recipient.account.update_balance(amount)
            
        except Exception as e:
            return e

    def validate_transaction(self, sender: Person, recipient: Person, amount: float):
        return recipient.account.get_details().owner == recipient.identity() and sender.account.get_details().owner == sender.identity() and amount != 0.0