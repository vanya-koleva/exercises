from datetime import date, timedelta


def all_sundays(year):
    dt = date(year, 1, 1)   # Set dt to January 1st of the given year
    # (6 - dt.weekday()) is the difference between the weekday of January 1st and Sunday
    dt += timedelta(days=6 - dt.weekday())  # the first Sunday of the year
    while dt.year == year:
        yield dt
        dt += timedelta(days=7)


for s in all_sundays(2024):
    print(s)
