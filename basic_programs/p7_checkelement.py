'''
@Author: Nagashree C R
@Date: 2024-07-12
@Last Modified by: Nagashree C R
@Last Modified: 2024-07-12
@Title : check whether a specified value is contained in a group of values.
'''


values=input("enter the value ").split(",")

values = [int(val) if val.isdigit() else val for val in values]

finding=input("enter the value to be found ")

print( finding in values)