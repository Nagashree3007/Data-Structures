'''
@Author: Nagashree C R
@Date: 2024-07-12
@Last Modified by: Nagashree C R
@Last Modified: 2024-07-12
@Title : Removing the frist Occurrence of the element
'''


def remove_first_occurrence(arr, element):
    """
    Description: Function to remove the element found at frist occurrence
    Parameter: 
        arr, element : function takes one array and one element
    Return:
    """


    if element in arr:
        arr.remove(element)


def main():
    arr = [1, 2, 3, 4, 2, 2, 3, 1, 1]
    element = 2

    print("**Original array** :----> ", arr)
    remove_first_occurrence(arr, element)
    print("**Array after removed** :--->", element, ":", arr)

