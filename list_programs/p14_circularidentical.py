"""

@Author: TarunSai
@Date: 2024-07-04
@Last Modified by: 
@Last Modified time:
@Title : Program to check whether two lists are circularly identical.

"""


def are_circularly_identical(list1, list2):

    """

    description:
        This function is used to check whether two lists are circularly identical.

    parameters:
        list1, Sample_test2(list) : list of elements.
        
    return:
        none

    """

    if len(list1) != len(list2):
        return False
    
    from itertools import permutations

    list2 = tuple([5, 4, 3, 2, 1])

    perm = permutations(list1)

    # print(list(perm))

    if list2 in list(perm):
        print("both are circularly identical")
    else:
        print("both are not circularly identical")
    


def main():

    list1 = [1, 2, 3, 4, 5]
    list2 = [3, 4, 5, 1, 2]
    are_circularly_identical(list1, list2)
    
if __name__ == "__main__":
    main()