"""

@Author: Nagashree C R
@Date: 2024-07-13
@Last Modified by: Nagashree C R
@Last Modified: 2024-07-13
@Title : Program to print a specified list after removing the 0th, 4th and 5th elements.

"""


def remove_items(Sample_list):

    """

    description:
        This function is used to print a specified list after removing the 0th, 4th and 5th elements.
    
    parameters:
        Sample_list(list) : list of elements.
        
    return:
        none

    """
    count = 0
    Sample_list.pop(0)
    for i in Sample_list:
        Sample_list.pop(-1)
        count+=1
        if count == 2:
            break
    print(Sample_list)

def main():
    Sample_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
    remove_items(Sample_list)


if __name__ == "__main__":
    main()