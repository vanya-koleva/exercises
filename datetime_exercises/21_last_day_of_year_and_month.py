import calendar

year = 2024
month = 5

# monthrange() -> (weekday of the first day of the month, number of days in the month)
print(calendar.monthrange(year, month)[1])
