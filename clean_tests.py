

import unittest
from ddt import ddt, data, unpack
from src.utils.general import AccountErrors
from src.entities.person import Person
from src.entities.account import Account
from src.services.current_account import CurrentAccountOperation 
from src.services.account_services import AccountOperations 
from src.operations.ted_operation import  TED
from src.models.entities import *

@ddt
class testApp(unittest.TestCase):
    
    @data(
        ('Fernando', '19/05/1997', 'Brazil', '43412314123', 100, 0, -50, 50, 'Miro', '18/03/1978', 'Brazil', '14312314123', 0, 0, 50, None),
        ('Fernando', '19/05/1997', 'Brazil', '43412314123', 100, 0, -50, 50, 'Miro', '18/03/1978', 'Brazil', '14312314123', -100, 200, -50, None),
        ('Fernando', '19/05/1997', 'Brazil', '43412314123', 100, 0, -100, 0, 'Miro', '18/03/1978', 'Brazil', '14312314123', 0, 0, 100, None),
        ('Fernando', '19/05/1997', 'Brazil', '43412314123', 100, 0, 0, 100, 'Miro', '18/03/1978', 'Brazil', '14312314123', 100, 0, 100, None),
        ('Fernando', '19/05/1997', 'Brazil', '43412314123', 100, 0, -200, 0, 'Miro', '18/03/1978', 'Brazil', '14312314123', 100, 0, 100, AccountErrors.NO_ENOUGH_LIMIT.value),
        ('Fernando', '19/05/1997', 'Brazil', '43412314123', 100, 100, -100, 0, 'Miro', '18/03/1978', 'Brazil', '14312314123', 0, 0, 100, None),
        ('Fernando', '19/05/1997', 'Brazil', '43412314123', 100, 100, -400, 0, 'Miro', '18/03/1978', 'Brazil', '14312314123', 0, 0, 100, AccountErrors.NO_ENOUGH_LIMIT.value),
    )
    @unpack
    def test_ted_transactions(self, p1_name, p1_bornd, p1_country, p1_identity, p1_start_balance, p1_start_special_credit, p1_amount_to_give, p1_expected_balance, p2_name, p2_bornd, p2_country, p2_identity, p2_start_balance, p2_start_special_credit, p2_expected_balance, error_to_expect):
        person1 = Person(
            p1_name,
            p1_bornd,
            p1_country,
            p1_identity
        )
        person1_account = Account(
            '123',
            'current',
            p1_start_balance,
            p1_start_special_credit
        )
        
        person2 = Person(
            p2_name,
            p2_bornd,
            p2_country,
            p2_identity
        )
        
        person2_account = Account(
            '321',
            'current',
            p2_start_balance,
            p2_start_special_credit
        )

        person1_account.set_owner(person1.identity())
        person2_account.set_owner(person2.identity())
        person1.add_account(person1_account)
        person2.add_account(person2_account)
        
        ted = TED()
        
        person1_current_operation = CurrentAccountOperation(person1, person2, ted)

        person1_operation = AccountOperations(person1, person1_current_operation)
        
        if error_to_expect is not None:
            with self.assertRaises(error_to_expect):
                person1_operation.update_balance(p1_amount_to_give)
                
        else:
            person1_operation.update_balance(p1_amount_to_give)
            self.assertEqual(person1.account.get_balance(), p1_expected_balance)
            self.assertEqual(person2.account.get_balance(), p2_expected_balance)
