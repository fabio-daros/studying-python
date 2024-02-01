"""
Working with deltas of date/time

Two dates to compare = deltas of date/time.

Example:
    date_init = dd/mm/yyyy 10:55:34.9939329
    date_end = dd/mm/yyyy 11:35:55.0945349

    delta = date_end - date_init
"""
# Example_1: ----------------------------------------------------------------

import datetime

"""

date_today = datetime.datetime.now()  # Actual date

birth_date = datetime.datetime(2024, 12, 29, 11)  # Date to the event occurs

time_event_start = birth_date - date_today  # calc the delta.

print(type(time_event_start))  # <class 'datetime.timedelta'>

print(repr(time_event_start))  # datetime.timedelta(days=-1796, seconds=28337, microseconds=194964)

print(time_event_start)

print(f'{time_event_start.days} days and {time_event_start.seconds // 60 // 60} hours left until the event.')
# To calculate the time difference and adjust the decimal points. With //60 //60.

"""
# Example_2: ----------------------------------------------------------------
# Example of a purchase in an e-commercial.

date_of_purchase = datetime.datetime.now()

print(date_of_purchase)

ticket_rule = datetime.timedelta(days=3)

print(ticket_rule)

ticket_expiration = date_of_purchase + ticket_rule

print(ticket_expiration)
