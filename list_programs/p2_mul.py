'''
@Author: Nagashree C R
@Date: 2024-07-13
@Last Modified by: Nagashree C R
@Last Modified: 2024-07-13
@Title : Program to to print multiply of all items in list.

'''


def multiply_of_list(list_of_numbers):

    """

    description:
        This function is used to print multiply of all items in list.
    
    parameters:
        list_of_numbers(set) : numbers in a set going to print in the function.
        
    return:
        none

    """

    product = 1
     
    for i in list_of_numbers:
        product*=i

    print(product)

def main():

    list_of_numbers = [1, 2, 3, 4]
    multiply_of_list(list_of_numbers)


if __name__ == "__main__":
    main()