import datetime as DT
from calendar import isleap


def days_calculator(year, month):
    if isleap(year):
        if month == 2:
            return 29
    elif month == 2:
        return 28
    odd_months = [1, 3, 5, 7, 8, 10, 12]
    if month in odd_months:
        return 31
    else:
        return 30


month1 = DT.datetime.now().month
year1 = DT.datetime.now().year

total_number_of_days = days_calculator(year1, month1)
half_of_month = int(total_number_of_days/2)
print(half_of_month)