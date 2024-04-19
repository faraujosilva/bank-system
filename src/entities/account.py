from src.models.entities import AccountModel
from src.utils.general import AccountErrors

class Account:
    def __init__(self, number: str, account_type: str, balance: float, special_credit: float = 0.0):
        self.__number = number
        self.__account_type = account_type
        self.__balance = balance
        self.__special_credit = special_credit
        self.owner = None
    
    def get_special_credit(self):
        return self.__special_credit

    def get_balance(self):
        if self.__have_owner:
            return self.__balance
    
    def get_details(self) ->  AccountModel:
        if self.__have_owner:
            return AccountModel(
            number=self.__number,
            balance=self.__balance,
            type = self.__account_type,
            owner=self.owner
            )

    def set_owner(self, person_identity: str):
        self.owner = person_identity
        
    def update_balance(self, amount: float):
        if self.__balance < 0 and amount < 0:
            self.__balance += amount
        else:
            self.__balance += amount
    
    @property
    def __have_owner(self):
        if self.owner is None:
            raise AccountErrors.NO_OWNER.value
        return True