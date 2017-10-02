
import Calculator
import datetime
from Calculator.datetime_manipulator import get_n_days_before_today
from Calculator.datetime_manipulator import get_todays_date
import unittest
import mock
from mock import Mock


@mock.patch('Calculator.datetime_manipulator.get_todays_date')
class date_test(unittest.TestCase):
    def test_n_days_before_today(self,mock_dt):
            mock_dt.return_value = datetime.date(2017,10,02)
            assert get_n_days_before_today(1) == datetime.date(2017,10,01)


