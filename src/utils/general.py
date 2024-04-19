from enum import Enum

class NoEnoughLimit(BaseException):
    def __init__(self, message: str):
        return super().__init__(message)
    
class NoOwner(BaseException):
    def __init__(self, message: str):
        return super().__init__(message)

class NoEnoughMoney(BaseException):
    def __int__(self, message: str):
        return super().__init__(message)

class AccountErrors(Enum):
    NO_ENOUGH_LIMIT = NoEnoughLimit('Client do not have enough special limit to do this operation')
    NO_OWNER = NoOwner('This Accont do not have any owner associated, invalid operation')
    NO_ENOUGH_MONEY = NoEnoughMoney('Client do not have enough money to do that operation')
    
class AccountInfo(Enum):
    SUCCESS_DEBIT = "Amount debited from account successfully"
    SUCCESS_CREDIT = "Amount credited  to account successfully"

class TEDInfo(Enum):
    START_TED = "Ted transaction started"