import datetime
from datetime import date


def add_years(d, years):
    try:
        return d.replace(year=d.year + years)
    # e.g., trying to go from February 29 to March 1 in a non-leap year
    except ValueError:
        # add the difference of the adjusted year's January 1st and the original Jan 1st
        return d + (date(d.year + years, 1, 1) - date(d.year, 1, 1))


print(add_years(datetime.date(2000, 2, 29), 1))
