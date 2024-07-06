import datetime


def display_current_datetime():
    global current_date
    current_date = datetime.datetime.now().date()
    print(f"Current date and time: {current_date}")


def calculate_future_date():
    display_current_datetime()
    number_days = int(input("Enter the number of days to add to the current date: "))
    future_date = current_date + datetime.timedelta(number_days)
    print(f"future date: {future_date}")


if __name__ == "__main__":
    calculate_future_date()
