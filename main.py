import argparse
import datetime
from datetime import date
from datetime import timedelta
import holidays
import calendar
from datetime import datetime
from typing import List


def get_weekends_in_month(year: int, month: int) -> int:
    count: int = 0
    month_days = date(year, month, 1)
    month_range = calendar.monthrange(year, month)
    for i in range(month_range[1]-1):
        if month_days.weekday() == 4 or month_days.weekday() == 5:
            count += 1
        month_days += timedelta(days=1)
    return count


def get_month_payable_holidays(year: int, month: int) -> List[datetime]:
    il_holidays = holidays.CountryHoliday('IL')
    month_range = calendar.monthrange(year, month)
    month_start = date(year, month, 1)
    month_end = date(year, month, month_range[1])
    all_holidays = [holiday for holiday in il_holidays[month_start:month_end] if holiday.weekday() != 4 or 5]
    payable_holidays = [holiday for holiday in all_holidays
                        if "Chol HaMoed".lower() not in il_holidays.get(holiday).lower()]
    return payable_holidays


def daily_spend() -> None:
    """
    Get how much you can spend daily on 10bis to not pass the limit.
    """
    parser = argparse.ArgumentParser(description=daily_spend.__doc__)

    parser.add_argument("-m", "--month", type=int)
    parser.add_argument("-i", "--monthly_income", type=int, required=True)
    parser.add_argument("-w", "--orders_in_week", type=int, required=True)
    parser.add_argument("-v", "--vacation_days", type=int, default=0)
    args = parser.parse_args()

    month = args.month or datetime.now().month
    year = datetime.now().year if datetime.now().month <= month else datetime.now().year
    days_in_month = calendar.monthrange(year, month)[1]
    orders_in_week = args.orders_in_week
    payable_holidays = get_month_payable_holidays(year, month)
    weekends_in_month = get_weekends_in_month(year, month)
    print(f'Your monthly 10bis budget is up to \
{int(args.monthly_income/(days_in_month-weekends_in_month-len(payable_holidays)-(5-orders_in_week)))} nis at day.')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    daily_spend()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
