"""

@Author: Nagashree C R
@Date: 2024-07-13
@Last Modified by: Nagashree C R
@Last Modified: 2024-07-13
@Title : Program to convert a list into a tuple.

"""

def create_tuple(list_of_numbers):

    """

    description:
        This function is used to convert a list into a tuple.
    
    parameters:
        list_of_numbers(list)) : list that we are converting into tuple.
        
    return:
        none

    """

    print(tuple(list_of_numbers))

def main():
    list_of_numbers = [1, 2, 3, 4]
    create_tuple(list_of_numbers)


if __name__ == "__main__":
    main()