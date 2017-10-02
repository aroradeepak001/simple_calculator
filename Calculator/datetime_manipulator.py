import datetime
from datetime import date

from datetime import timedelta

def get_todays_date():
    return date.today()

def get_n_days_before_today(n):
    timedelta_n_days = timedelta(days=n)
    return get_todays_date()-timedelta_n_days