import pytest

from domain.models import Stock

@pytest.mark.unitest
def test_stock():
    s = Stock(
        name='0050.TW',
        bid=1.1,
        pre_close=2.2,
        day_high=3.3,
        day_low=4.4,
        year_high=5.5,
        year_low=6.6
    )

    assert s.name == '0050.TW'
    assert s.bid == 1.1
    assert s.pre_close == 2.2
    assert s.day_high == 3.3
    assert s.day_low == 4.4
    assert s.year_high == 5.5
    assert s.year_low == 6.6

@pytest.mark.unitest
def test_stock__format_to_message():
    s = Stock(
        name='0050.TW',
        bid=1.1,
        pre_close=2.2,
        day_high=3.3,
        day_low=4.4,
        year_high=5.5,
        year_low=6.6
    )

    assert s.format_to_message() == '0050.TW\n目前：1.1\n作收：2.2\n最高：3.3\n最低：4.4\n52周最高：5.5\n52周最低：6.6'