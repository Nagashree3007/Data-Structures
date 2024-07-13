"""

@Author: TarunSai
@Date: 2024-07-04
@Last Modified by: 
@Last Modified time:
@Title : Program to clone a list.

"""


def clone_list(list_of_numbers):

    """

    description:
        This function is used to clone list.
    
    parameters:
        list_of_numbers(list)) : numbers in list we are printing.
        
    return:
        none

    """

    cloned_list = list_of_numbers.copy()#shallow copy

    import copy
    cloned_list_1 = copy.deepcopy(list_of_numbers)#deep copy

    print(cloned_list)
    print(id(cloned_list))
    print(id(list_of_numbers))
    print(cloned_list_1)
    print(id(cloned_list_1))
    print(id(list_of_numbers))

def main():

    global list_of_numbers
    list_of_numbers = [1, 2, 3, 4, (1,3)]
    clone_list(list_of_numbers)


if __name__ == "__main__":
    main()