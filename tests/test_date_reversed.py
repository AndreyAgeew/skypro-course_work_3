from utils import date_reversed


def test_date_reversed():
    assert date_reversed('2022-01-01T12:00:00') == "01.01.2022"
