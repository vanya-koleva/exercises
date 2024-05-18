from datetime import datetime, date

d = date.today()

print(datetime.combine(d, datetime.min.time()))
