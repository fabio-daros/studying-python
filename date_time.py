"""
Manipulation Date and Time

Python has a builtIn to work with date and time called datetime.
"""

import datetime

# print(dir(datetime))

print(datetime.MAXYEAR)  # Max year of date time supported = 9999.

print(datetime.MINYEAR)  # Min year of date time supported = 1.

print(datetime.datetime.now())  # return current datetime = 2024-01-31 15:23:54.297176.

print(repr(datetime.datetime.now()))  # datetime.datetime(year, month, day, hour, minute, second, microsecond)

# replace() to adjust date/time.

init = datetime.datetime.now()

print(init)

# alter the time to 4h, 0min, 0sec, 0mcs.

init = init.replace(hour=4, minute=0, second=0, microsecond=0)  # To program the time to execute something.

print(init)

# Create a date/time object

event = datetime.datetime(2024, 1, 1, 0)

print(type(event))

print(type('31/12/2023'))

birth_day = input('Enter your birth date (DD/MM/YYYY): ')
# Received datas from the user and converted to date.
birth_day = birth_day.split('/')

birth_day = datetime.datetime(int(birth_day[2]), int(birth_day[1]), int(birth_day[0]))

print(birth_day)

print(type(birth_day))

# Access individual attributes from elements of date/time.

event_2 = datetime.datetime.now()

print(event_2.year)
print(event_2.month)
print(event_2.day)
print(event_2.hour)
print(event_2.minute)
print(event_2.second)
print(event_2.microsecond)
