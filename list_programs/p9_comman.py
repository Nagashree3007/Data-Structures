"""

@Author: Nagashree C R
@Date: 2024-07-13
@Last Modified by: Nagashree C R
@Last Modified: 2024-07-13
@Title : Program that takes two lists and returns True if they have at least one common member.

"""


def common_member(Sample_list1, Sample_list2):

    """

    description:
        This function is used least one common member least one common member. 
           
    parameters:
        Sample_list1, Sample_test2(list) : list of elements.
        
    return:
        none

    """
    
    for i in Sample_list1:
        if i in Sample_list2:
            return True

def main():
    Sample_list1 = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
    Sample_list2 = ['Red', 'Green', 'White', 'Pink']
    
    common_member_in_list = common_member(Sample_list1, Sample_list2)
    print(common_member_in_list)
    


if __name__ == "__main__":
    main()