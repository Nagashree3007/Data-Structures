'''
@Author: Nagashree C R
@Date: 2024-07-12
@Last Modified by: Nagashree C R
@Last Modified: 2024-07-12
@Title : concatenate all elements in a list into a string and return it.
'''

values=input("enter the list elements").split(',')

values=list(values)

print(values)

string_con=''

for val in values:
    string_con+=val+' '
    
print(string_con)