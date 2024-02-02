"""
Date / Time Methods

"""

# Example_1 ----------------------------------------------------------------

import functools
import timeit

"""
now = datetime.datetime.now()  # With now, its possible put a timezone.

print(now)
print(type(now))
print(repr(now))

today = datetime.datetime.today()  # With today, its not possible put a timezone.

print(today)
print(type(today))
print(repr(today))
"""
# Example_2 ----------------------------------------------------------------
# Changes occurred at midnight. (combine())
"""
# The week days of the method weekday() starts from 0 - monday

# 0 - Monday
# 1 - Tuesday
# 2 - Wednesday
# 3 - Thursday
# 4 - Friday
# 5 - Saturday
"""
"""
maintenance = datetime.datetime.combine((datetime.datetime.now() + datetime.timedelta(days=1)), datetime.time())
# 1 day ahead.

print(maintenance.weekday())
"""
# Example_3 ----------------------------------------------------------------
# Function to see the weekday of the method weekday() from a valid date.
"""
birth_day = input('Enter your birthday (dd/mm/yyyy): ')

birth_day = birth_day.split('/')

birth_day = datetime.datetime(year=int(birth_day[2]), month=int(birth_day[1]), day=int(birth_day[0]))

if birth_day.weekday() == 0:
    print('You born in a monday.')
elif birth_day.weekday() == 1:
    print('You born in a tuesday.')
elif birth_day.weekday() == 2:
    print('You born in a wednesday.')
elif birth_day.weekday() == 3:
    print('You born in a thursday.')
elif birth_day.weekday() == 4:
    print('You born in a friday.')
elif birth_day.weekday() == 5:
    print('You born in a saturday.')
elif birth_day.weekday() == 6:
    print('You born in a sunday.')
"""
# Example_4 ----------------------------------------------------------------
# Format date/hours with "strf time()" String formatting Time
"""
today = datetime.datetime.today()

print(today)

today_formatted = today.strftime('%Y/%B/%d')

print(f'Formatted date: {today_formatted}')  # 2024/February/01
"""

# To know more about: https://docs.python.org/3/library/datetime.html

# Example_5 ----------------------------------------------------------------
# A better example to format creating a function:
"""
def format_date(date):
    if date.month == 1:
        return f'{date.day} January {date.year}.'
    elif date.month == 2:
        return f'{date.day} February {date.year}.'
    elif date.month == 3:
        return f'{date.day} March {date.year}.'
    elif date.month == 4:
        return f'{date.day} April {date.year}.'
    elif date.month == 5:
        return f'{date.day} May {date.year}.'
    elif date.month == 6:
        return f'{date.day} June {date.year}.'
    elif date.month == 7:
        return f'{date.day} July {date.year}.'
    elif date.month == 8:
        return f'{date.day} August {date.year}.'
    elif date.month == 9:
        return f'{date.day} September {date.year}.'
    elif date.month == 10:
        return f'{date.day} October {date.year}.'
    elif date.month == 11:
        return f'{date.day} November {date.year}.'
    elif date.month == 12:
        return f'{date.day} December {date.year}.'


today = datetime.datetime.today()

print(f'Formatted date with a function: {format_date(today)}')
"""

# Example_6 ----------------------------------------------------------------

"""
from textblob import TextBlob


def format_date_2(date_2):
    return f'{date_2.day} {TextBlob(date_2.strftime('%B')).translate(to='pt-br')} {date_2.year}'


today = datetime.datetime.today()

print(f'Formatted date with a google: {format_date_2(today)}')
"""

# Example_7 ----------------------------------------------------------------
# Pythonic form to work with dates.
"""
born_day = datetime.datetime.strptime('2024/02/01', '%Y/%m/%d')

print(born_day)

born_day = input('Enter your born day (yyyy/mm/dd): ')

born_day = datetime.datetime.strptime(born_day, '%Y/%m/%d')

print(born_day)
"""

# Example_8 ----------------------------------------------------------------
# Work with hours.

"""
launch_time = datetime.time(12, 30, 0)

print(launch_time)
"""

# Example_9 ----------------------------------------------------------------
# Mark the execution time of the code with timeit to available.

# Loop for:
"""
time_count = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)  # put the '-' in numbers x10000.
print(time_count)  # 0.1972370139992563

# List Comprehension:

time_count_lc = timeit.timeit('[str(n) for n in range(100)]', number=10000)
print(time_count_lc)  # 0.10589436200098135

# Map:
time_count_map = timeit.timeit('"-".join(map(str, range(100)))', number=10000)
print(time_count_map)  # 0.15033833099005278
"""


# Example_10 ----------------------------------------------------------------
# functools
# ** THE BEST FORM TO TEST THE EXECUTION SPEED OF A FUNCTION.

def test(n):
    sum_1 = 0
    for num in range(n * 200):
        sum_1 = sum_1 + num ** num + 4
    return sum_1


print(timeit.timeit(functools.partial(test, 2), number=10000))
# 7.8894031009986065
