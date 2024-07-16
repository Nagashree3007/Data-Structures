'''


@Author: Nagashree C R
@Date: 2024-07-12
@Last Modified by: Nagashree C R
@Last Modified: 2024-07-12 
@Title : Reverse the order of items in the Array


'''

array_of_integers = list(map(int,input("enter the elements in array").split(',')))
print("Original array:--->", array_of_integers)
#for reversing the elements
reversed_array = array_of_integers[::-1]
array2_integers =reversed_array
print("Reversed array:--->", array2_integers )
