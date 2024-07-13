'''
@Author: Nagashree C R
@Date: 2024-07-12
@Last Modified by: Nagashree C R
@Last Modified: 2024-07-12
@Title :Python program to print the calendar of a given month and year.
'''




import calendar

def print_calendar(year, month):
    # Using the month() method to get the calendar
    cal = calendar.month(year, month)
    
    # Print the calendar
    print(f"Calendar for {calendar.month_name[month]} {year}:")
    print(cal)
# Input month and year (you can change these values as needed)
year =  int(input())
month = int(input())

# Call the function to print the calendar
print_calendar(year, month)
