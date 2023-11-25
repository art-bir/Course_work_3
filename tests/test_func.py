import pytest
from utils import *


@pytest.mark.parametrize('a, expected_result',
                         [('tests/test_operations.json', [{"key_1": "value_1"}, {"key_2": "value_2"}]),
                          ('', None)])
def test_read_json(a, expected_result):
    assert read_json(file=a) == expected_result


@pytest.mark.parametrize('a, expected_result', [('2019-08-26T10:50:58.294041', '26.08.2019'),
                                                ('2019-07-03T18:35:29.512364', '03.07.2019')])
def test_trans_date(a, expected_result):
    assert trans_date(a) == expected_result


@pytest.mark.parametrize('a, expected_result', [('Maestro 1596837868705199', ('Maestro ', '1596837868705199')),
                                                ('MasterCard 7158300734726758', ('MasterCard ', '7158300734726758')),
                                                ('Счет 75106830613657916952', ('Счет ', '75106830613657916952'))])
def test_check_alpha_digit(a, expected_result):
    assert split_name_and_number(a) == expected_result


@pytest.mark.parametrize('a, b, expected_result', [('Maestro 1596837868705199', 'from', 'Maestro 1596 37** **** 5199'),
                                                   ('Maestro 1596837868705199', 'to', 'Maestro  **5199'),
                                                   ('MasterCard 7158300734726758', 'from',
                                                    'MasterCard 7158 00** **** 6758'),
                                                   ('MasterCard 7158300734726758', 'to', 'MasterCard  **6758')])
def test_trans_card_account(a, b, expected_result):
    assert masks_number(a, b) == expected_result


@pytest.mark.parametrize('a, expected_result', [(
        [{"state": "EXECUTED", "description": "Перевод организации", },
         {"state": "CANCELED", "date": "2018-09-12T21:27:25.241689", }],
        [{'description': 'Перевод организации', 'state': 'EXECUTED'}])])
def test_get_executed_transaction_list(a, expected_result):
    assert get_executed_transaction_list(a) == expected_result
