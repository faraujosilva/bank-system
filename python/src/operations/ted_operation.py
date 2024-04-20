from src.entities.person import Person
from src.interfaces.iaccountmethod import IOperationMethod
from src.utils.general import TEDInfo

class TED(IOperationMethod):
    def do_transaction(self, sender: Person, recipient: Person, amount: float):
        print(TEDInfo.START_TED.value)

        try:
            if self.validate_transaction(sender, recipient, amount):
                sender.account.update_balance(amount)
                recipient.account.update_balance(amount)
            
        except Exception as e:
            return e

    def validate_transaction(self, sender: Person, recipient: Person, amount: float):
        return recipient.account.get_details().owner == recipient.identity() and sender.account.get_details().owner == sender.identity() and amount != 0.0