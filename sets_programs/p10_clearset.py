"""

@Author: Nagashree C R
@Date: 2024-07-13
@Last Modified by: Nagashree C R
@Last Modified: 2024-07-13
@Title : Program to clear set.

"""

def clear_set(numbers):

    """

    description:
        This function is used clear an set.
    
    parameters:
        numbers : set that is going to clear.
        
    return:
        none

    """
    numbers.clear()
    print(numbers)
          

def main():
    numbers = {1, 2, 3, 4, 5}
    clear_set(numbers)


if __name__ == "__main__":
    main()