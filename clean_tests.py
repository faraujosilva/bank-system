

import unittest
from ddt import ddt, data, unpack
from src.utils.general import AccountErrors
from src.entities.person import Person
from src.entities.account import Account
from src.services.current_account import CurrentAccountOperation 
from src.services.account_services import AccountServices 
from src.operations.ted_operation import TED
from src.operations.pix_operation import PIX
from src.models.entities import *

@ddt
class testApp(unittest.TestCase):
    
    @data(
        ('Fernando', '19/05/1997', 'Brazil', '43412314123', 100, 0, -50, 50, 'Miro', '18/03/1978', 'Brazil', '14312314123', 0, 0, 50, None, TED()),
        ('Fernando', '19/05/1997', 'Brazil', '43412314123', 100, 0, -50, 50, 'Miro', '18/03/1978', 'Brazil', '14312314123', -100, 200, -50, None, TED()),
        ('Fernando', '19/05/1997', 'Brazil', '43412314123', 100, 0, -100, 0, 'Miro', '18/03/1978', 'Brazil', '14312314123', 0, 0, 100, None, TED()),
        ('Fernando', '19/05/1997', 'Brazil', '43412314123', 100, 0, 0, 100, 'Miro', '18/03/1978', 'Brazil', '14312314123', 100, 0, 100, None, TED()),
        ('Fernando', '19/05/1997', 'Brazil', '43412314123', 100, 0, -200, 0, 'Miro', '18/03/1978', 'Brazil', '14312314123', 100, 0, 100, AccountErrors.NO_ENOUGH_LIMIT.value, TED()),
        ('Fernando', '19/05/1997', 'Brazil', '43412314123', 100, 100, -100, 0, 'Miro', '18/03/1978', 'Brazil', '14312314123', 0, 0, 100, None, TED()),
        ('Fernando', '19/05/1997', 'Brazil', '43412314123', 100, 100, -400, 0, 'Miro', '18/03/1978', 'Brazil', '14312314123', 0, 0, 100, AccountErrors.NO_ENOUGH_LIMIT.value, TED()),
        
        ('Fernando', '19/05/1997', 'Brazil', '43412314123', 100, 0, -50, 50, 'Miro', '18/03/1978', 'Brazil', '14312314123', 0, 0, 50, None, PIX()),
        ('Fernando', '19/05/1997', 'Brazil', '43412314123', 100, 0, -50, 50, 'Miro', '18/03/1978', 'Brazil', '14312314123', -100, 200, -50, None, PIX()),
        ('Fernando', '19/05/1997', 'Brazil', '43412314123', 100, 0, -100, 0, 'Miro', '18/03/1978', 'Brazil', '14312314123', 0, 0, 100, None, PIX()),
        ('Fernando', '19/05/1997', 'Brazil', '43412314123', 100, 0, 0, 100, 'Miro', '18/03/1978', 'Brazil', '14312314123', 100, 0, 100, None, PIX()),
        ('Fernando', '19/05/1997', 'Brazil', '43412314123', 100, 0, -200, 0, 'Miro', '18/03/1978', 'Brazil', '14312314123', 100, 0, 100, AccountErrors.NO_ENOUGH_LIMIT.value, PIX()),
        ('Fernando', '19/05/1997', 'Brazil', '43412314123', 100, 100, -100, 0, 'Miro', '18/03/1978', 'Brazil', '14312314123', 0, 0, 100, None, PIX()),
        ('Fernando', '19/05/1997', 'Brazil', '43412314123', 100, 100, -400, 0, 'Miro', '18/03/1978', 'Brazil', '14312314123', 0, 0, 100, AccountErrors.NO_ENOUGH_LIMIT.value, PIX()),

    )
    @unpack
    def test_ted_transactions(self, p1_name, p1_bornd, p1_country, p1_identity, p1_start_balance, p1_start_special_credit, p1_amount_to_give, p1_expected_balance, p2_name, p2_bornd, p2_country, p2_identity, p2_start_balance, p2_start_special_credit, p2_expected_balance, error_to_expect, pay_method):
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
        
        person1_current_operation = CurrentAccountOperation(person1, person2, pay_method)

        person1_operation = AccountServices(person1, person1_current_operation)
        
        if error_to_expect is not None:
            with self.assertRaises(error_to_expect):
                person1_operation.update_balance(p1_amount_to_give)
                
        else:
            person1_operation.update_balance(p1_amount_to_give)
            self.assertEqual(person1.account.get_balance(), p1_expected_balance)
            self.assertEqual(person2.account.get_balance(), p2_expected_balance)
            
