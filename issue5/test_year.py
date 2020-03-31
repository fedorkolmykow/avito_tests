import pytest
from unittest.mock import MagicMock
import urllib.request
import what_is_year_now


@pytest.mark.parametrize('date, exp', [
    ({'currentDateTime': '2001-03-01'}, 2001),
    ({'currentDateTime': '01.03.9999'}, 9999),
])
def test_all():
    date = {'currentDateTime': '2001-03-01'}
    urllib.request.urlopen = MagicMock
    urllib.request.urlopen.return_value.__enter__.return_value = date
    print(what_is_year_now.what_is_year_now())



