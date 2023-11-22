import pytest

from utils.func import trans_date


@pytest.mark.parametrize('a, expected_result', [('2019-08-26T10:50:58.294041', '26.08.2019'),
                                                ('2019-07-03T18:35:29.512364', '03.07.2019')])
def test_trans_date(a, expected_result):
    assert trans_date(a) == expected_result
