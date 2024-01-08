import time
from datetime import datetime


def calculate_age(birthdate):
    try:
        birthdate = datetime.strptime(birthdate, "%Y-%m-%d")
        today = datetime.today()
        age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
        return age
    except ValueError:
        print("Invalid date format. Please use 'YYYY-MM-DD'")
        time.sleep(1)
        print("Try again...")
        return None


def main():
    print("Enter your name:")
    name = input()

    print("Enter your birth date (YYYY-MM-DD):")
    birthdate = input()

    age = calculate_age(birthdate)

    if age is not None:
        print(f'Hello, {name}! You are {age} years old.')
        # Additional format options:
        # print(f'{name}, you were born on {birthdate} and you are {age} years old.')
        # print(f'Today, {name} is celebrating their {age}th birthday!')
    else:
        main()


if __name__ == "__main__":
    main()
