'''
@Author: Nagashree C R
@Date: 2024-07-12
@Last Modified by: Nagashree C R
@Last Modified: 2024-07-12
@Title : accepts the user's first and last name and print them in
reverse order with a space between them.
'''


def reverse(s):
    return(s[::-1])


first_name=input("enter first name")
last_name=input("enter first name")
print(f'{last_name} {first_name}')
print(f'{reverse(last_name)} {reverse(first_name)}')