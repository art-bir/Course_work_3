import pytest
from utils import *


@pytest.mark.parametrize('a, expected_result', [('2019-08-26T10:50:58.294041', '26.08.2019'),
                                                ('2019-07-03T18:35:29.512364', '03.07.2019')])
def test_trans_date(a, expected_result):
    assert trans_date(a) == expected_result


@pytest.mark.parametrize('a, expected_result', [('Maestro 1596837868705199', ('Maestro ', '1596837868705199')),
                                                ('MasterCard 7158300734726758', ('MasterCard ', '7158300734726758')),
                                                ('Счет 75106830613657916952', ('Счет ', '75106830613657916952'))])
def test_check_alpha_digit(a, expected_result):
    assert check_alpha_digit(a) == expected_result


@pytest.mark.parametrize('a, b, expected_result', [('Maestro 1596837868705199', 'from', 'Maestro 1596 37** **** 5199'),
                                                   ('Maestro 1596837868705199', 'to', 'Maestro  **5199'),
                                                   ('MasterCard 7158300734726758', 'from',
                                                    'MasterCard 7158 00** **** 6758'),
                                                   ('MasterCard 7158300734726758', 'to', 'MasterCard  **6758')])
def test_trans_card_account(a, b, expected_result):
    assert trans_card_account(a, b) == expected_result
