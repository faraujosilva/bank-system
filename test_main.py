from src.entities.person import Person
from src.entities.account import Account
from src.services.current_account import CurrentAccountOperation 
from src.services.account_services import AccountOperations 
from src.operations.ted_operation import  TED
from src.models.entities import *

    
me = Person(
    'Fernando',
    '19/05/1997',
    'Brazil',
    '4321123123123'
)

account = Account(
    '123',
    'current',
    1000.0,
    0.0
)
account.set_owner(me.identity())
me.add_account(account)

miro = Person(
    'Miro',
    '01/01/1990',
    'Brazil',
    '123123123123'
)

miro_acc = Account(
    '124',
    'current',
    300.0,
    0.0
)

miro_acc.set_owner(miro.identity())
miro.add_account(miro_acc)

assert me.account.get_balance() == 1000.0
assert isinstance(me.account.get_details(), AccountModel)
assert isinstance(me.details(), PersonModel)
assert me.name() == 'Fernando'
assert me.account is not None
assert me.account.get_details().number == '123'

ted = TED()
me_current_account = CurrentAccountOperation(me, miro, ted)

me_account_operation = AccountOperations(me, me_current_account)

me_account_operation.update_balance(-99.0)

assert me.account.get_balance() == 901
assert miro.account.get_balance() == 399
