"""

@Author: Nagashree C R
@Date: 2024-07-13
@Last Modified by: Nagashree C R
@Last Modified: 2024-07-13
@Title : Program to remove an item in set if it is present.

"""

def remove_set(numbers, item):

    """

    description:
        This function is used remove an item in set if it is present.
    
    parameters:
        numbers(set) : numbers in set that are used for iteration and remove from the set.
        
    return:
        none

    """
    
    for i in numbers:
        if i == item:
            numbers.remove(item)
    print(numbers)
          

def main():
    item = int(input("enter a item: "))
    numbers = [1, 2, 3, 4, 5]
    remove_set(numbers, item)


if __name__ == "__main__":
    main()