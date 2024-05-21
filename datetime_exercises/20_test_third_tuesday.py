from datetime import datetime


def is_third_tuesday(s):
    dt = datetime.strptime(s, '%b %d, %Y')
    return dt.weekday() == 1 and 14 < dt.day < 22


print(is_third_tuesday('May 21, 2024'))
print(is_third_tuesday('May 14, 2024'))
