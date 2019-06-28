from datetime import datetime
from datetime import date


print(datetime.today())
print(type(datetime.today()))

print()
todaydate = date.today()
print(todaydate.year)
print(todaydate.month)
print(todaydate.day)

print()
christmas = date(2020, 1, 7)
print("It's still {} days until Christmas!".format((christmas -
                                                   todaydate).days))

# Time delta

from datetime import timedelta

print()
t = timedelta(days=4, hours=10)
print(type(t))
print(t.seconds)
print(t.seconds / 60 / 60)    # Hours

print()
eta = timedelta(hours=6)
today = datetime.today()
print(eta)
print(today)
print((today + eta).day == today.day)  # Check whether same day after adding  

