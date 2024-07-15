"""

@Author: Nagashree C R
@Date: 2024-07-13
@Last Modified by: Nagashree C R
@Last Modified: 2024-07-13
@Title : Program that takes lists and returns permutation of each element in list.

"""


def generate_permutations(input_list):

    """

    description:
        This function is used to returns permutation of each element in list.
    
    parameters:
        Sample_list(list) : list of elements.
        
    return:
        perm_list

    """
    
    from itertools import permutations

    perm = permutations(input_list)
    perm_list = list(perm)
    
    return perm_list

def main():

    input_list = [1, 2, 3]
    print("Input List:", input_list)
    print("Permutations:")
    for perm in generate_permutations(input_list):
        print(perm)

if __name__ == "__main__":
    main()




