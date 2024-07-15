"""

@Author: TarunSai
@Date: 2024-07-04
@Last Modified by: 
@Last Modified time:
@Title : Program to get the difference between the two lists.

"""


def uncommon_items(Sample_list1, Sample_list2):

    """

    description:
        This function is used to get the difference between the two lists.
    
    parameters:
        Sample_list1, Sample_test2(list) : list of elements.
        
    return:
        none

    """
    Sample_list = []
    for i in Sample_list1:
        if i not in Sample_list2:
            Sample_list.append(i)
    print(Sample_list)

def main():

    global Sample_list1, Sample_list2 
    Sample_list1 = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
    Sample_list2 = ['Red', 'Green', 'White', 'Pink']
    
    uncommon_items(Sample_list1, Sample_list2)
    


if __name__ == "__main__":
    main()