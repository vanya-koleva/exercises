from datetime import datetime, date

# The "isocalendar()" method returns a tuple containing year, week number, and weekday.
week_n = date(2015, 6, 16). isocalendar()[1]

print(week_n)