from enum import Enum

class NoEnoughLimit(BaseException):
    def __init__(self, message: str='Client do not have enough special limit to do this operation'):
        return super().__init__(message)
    
class NoOwner(BaseException):
    def __init__(self, message: str='This Accont do not have any owner associated, invalid operation'):
        return super().__init__(message)

class NoEnoughMoney(BaseException):
    def __int__(self, message: str='Client do not have enough money to do that operation'):
        return super().__init__(message)

class AccountErrors(Enum):
    NO_ENOUGH_LIMIT = NoEnoughLimit
    NO_OWNER = NoOwner
    NO_ENOUGH_MONEY = NoEnoughMoney
    
class AccountInfo(Enum):
    SUCCESS_DEBIT = "Amount debited from account successfully"
    SUCCESS_CREDIT = "Amount credited  to account successfully"

class TEDInfo(Enum):
    START_TED = "Ted transaction started"

class PIXInfo(Enum):
    START_PIX = "PIX transaction started"

