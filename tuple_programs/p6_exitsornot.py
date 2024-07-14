"""

@Author: Nagashree C R
@Date: 2024-07-13
@Last Modified by: Nagashree C R
@Last Modified: 2024-07-13
@Title : Program to check whether an element exists within a tuple.

"""

def element_in_tuple(tuple_of_numbers, element):

    """

    description:
        This function to check whether an element exists within a tuple.
    
    parameters:
        tuple_of_numbers(tuple)) : tuple to check the element is exsists.
        
    return:
        none

    """
    for i in tuple_of_numbers:
        if i == element:
            print(element, "element exists")
            break
        else:
            print(element, "not exists")
            break
            
    


def main():

    global tuple_of_numbers, element
    element = int(input("enter a number: "))
    tuple_of_numbers = (1, 1, 2, 3, 4)
    element_in_tuple(tuple_of_numbers, element)


if __name__ == "__main__":
    main()