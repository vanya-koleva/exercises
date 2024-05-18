from datetime import datetime, timedelta

starting_date = datetime.today()

for x in range(1, 5 + 1):
    print(starting_date + timedelta(x))
