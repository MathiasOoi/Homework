from datetime import date
from collections import defaultdict

x = defaultdict(int)
for year in range(1901, 2001):
    for month in range(1, 13):
        x[date(year, month, 1).weekday()] += 1
print(x)
print(x[6])