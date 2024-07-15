"""
@Author: Nagashree C R
@Date: 2024-07-13
@Last Modified by: Nagashree C R
@Last Modified: 2024-07-13
@Title : Program to add numbers to the sets.

"""

def add_set(numbers):

    """

    description:
        This function is used to add numbers sets.
    
    parameters:
        numbers(set) : numbers in set that are used for iteration and adding to set.
        
    return:
        none

    """
    elements = set()

    for i in numbers:
        elements.add(i)

    print(elements)       

def main():
    numbers = [1, 2, 3, 4, 5]
    add_set(numbers)


if __name__ == "__main__":
    main()