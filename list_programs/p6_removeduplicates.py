"""

@Author: TarunSai
@Date: 2024-07-04
@Last Modified by: 
@Last Modified time: 
@Title : Program to remove duplicates from a list.

"""


def remove_duplicates(numbers):

    """

    description:
        This function is used to remove duplicates from a list.
    
    parameters:
        numbers(list) : list going to remove duplicates.
        
    return:
        none

    """

    no_duplicates = []
    for i in numbers:
        if i not in no_duplicates:
            no_duplicates.append(i)
    print(no_duplicates)


def main():

    
    numbers = [1, 1, 3, 5, 83, 0]
    remove_duplicates(numbers)


if __name__ == "__main__":
    main()