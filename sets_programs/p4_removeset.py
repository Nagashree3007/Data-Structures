"""

@Author: Nagashree C R
@Date: 2024-07-13
@Last Modified by: Nagashree C R
@Last Modified: 2024-07-13
@Title : Program to remove elements sets.

"""

def remove_set(numbers):

    """

    description:
        This function is used to remove elements sets.
    
    parameters:
        numbers(set) : numbers in set that are used for iteration and adding to set.
        
    return:
        none

    """

    numbers.remove(1)
    numbers.remove(2)

    print(numbers)       

def main():
    numbers = {1, 2, 3, 4, 5}
    remove_set(numbers)


if __name__ == "__main__":
    main()