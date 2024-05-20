from datetime import datetime

today = datetime.now()
day_of_year = (today - datetime(today.year, 1, 1)).days + 1

print(day_of_year)
