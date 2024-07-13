'''
@Author: Nagashree C R
@Date: 2024-07-12
@Last Modified by: Nagashree C R
@Last Modified: 2024-07-12
@Title : program to display the first and last colors from the following list.
'''


values=list(map(str,input("enter the colours ").split(",")))
print(values)
print(f'the first colour is {values[0]} and colour at the last is {values[len(values)-1]} ')