from datetime import date, timedelta

date_needed = date.today() - timedelta(5)
print("Current date:", date.today())
print("5 days before today:", date_needed)
