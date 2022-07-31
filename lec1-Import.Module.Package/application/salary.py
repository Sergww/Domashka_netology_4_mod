from datetime import datetime

def calculate_salary():
    dates = datetime.now()
    print('calculate_salary = ', dates)
    print('day, month, year = ', dates.day, dates.month, dates.year)