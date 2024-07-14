"""

@Author: Nagashree C R
@Date: 2024-07-13
@Last Modified by: Nagashree C R
@Last Modified: 2024-07-13
@Title : Program to reverse a tuple.

"""

def reverse_tuple(tuple_of_numbers):

    """

    description:
        This function is used to reverse tuple.
    
    parameters:
        tuple_of_numbers(tuple)) : numbers in tuple we are printing.
        
    return:
        none

    """

    print(tuple_of_numbers[::-1])

def main():
    tuple_of_numbers = (1, 2, 3, 4)
    reverse_tuple(tuple_of_numbers)


if __name__ == "__main__":
    main()