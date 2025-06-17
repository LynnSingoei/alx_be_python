from datetime import datetime, timedelta

def display_current_datetime():
    current_date=datetime.now()
    print(f"Current date and time: {current_date.strftime('%Y-%m-%d %H:%M:%S')}")

days=input("Enter the number of days to add to the current date: ")
def calculate_furure_date():
    cur_date=datetime.today().date()
    future_date=cur_date+ timedelta(days=int(days))
    print(f"Future date is:{future_date.strftime('%Y-%m-%d')}")

