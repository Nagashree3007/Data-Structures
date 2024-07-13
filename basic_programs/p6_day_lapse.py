'''
@Author: Nagashree C R
@Date: 2024-07-12
@Last Modified by: Nagashree C R
@Last Modified: 2024-07-12
@Title :calculate number of days between two dates.
'''


from datetime import date

def days_between_dates(date1, date2):
    # Convert input tuples to date objects
    date1_obj = date(date1[0], date1[1], date1[2])
    date2_obj = date(date2[0], date2[1], date2[2])
    
    # Calculate the difference between two dates
    delta = date2_obj - date1_obj
    
    # Return the number of days (absolute value in case date2 is before date1)
    return abs(delta.days)

# Sample dates
date1 = list(map(int,input("YYYY-MM-DD").split("-")))
date2 =  list(map(int,input("YYYY-MM-DD").split("-")))

# Calculate and print the number of days between the two dates
days = days_between_dates(date1, date2)
print(f"Number of days between {date1} and {date2}: {days} days")
