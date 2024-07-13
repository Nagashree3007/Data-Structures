"""

@Author: Nagashree C R
@Date: 2024-07-13
@Last Modified by: Nagashree C R
@Last Modified: 2024-07-13
@Title : Program to remove duplicate items from list.

"""


def rempove_duplicate_items(Sample_list):

    """

    description:
        This function is used to remove duplicate items from list.
    
    parameters:
        Sample_list(list) : list of elements.
        
    return:
        none

    """
    no_duplicates = []
    for i in Sample_list:
        if i not in no_duplicates:
            no_duplicates.append(i)
    print(no_duplicates)

def main():
    Sample_list = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
    
    rempove_duplicate_items(Sample_list)
    


if __name__ == "__main__":
    main()