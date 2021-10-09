# 10bis_monthly_spend

external packeges: https://pypi.org/project/holidays/

usage: main.py [-h] [-m MONTH] -i MONTHLY_INCOME -w ORDERS_IN_WEEK [-v VACATION_DAYS]

Get how much you can spend daily on 10bis to not pass the limit.

optional arguments:
  -h, --help            show this help message and exit
  -m MONTH, --month MONTH
  -i MONTHLY_INCOME, --monthly_income MONTHLY_INCOME
  -w ORDERS_IN_WEEK, --orders_in_week ORDERS_IN_WEEK
  -v VACATION_DAYS, --vacation_days VACATION_DAYS

For example:
>>> "./main.py" -i 900 -w 5 -m 10
Your monthly 10bis budget is up to 42 nis at day.
