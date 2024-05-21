from datetime import date, timedelta

today = date.today()
offset = (today.weekday() - 1) % 7
last_tuesday = today - timedelta(days=offset)

print(last_tuesday)
