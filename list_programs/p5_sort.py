"""
@Author: Nagashree C R
@Date: 2024-07-13
@Last Modified by: Nagashree C R
@Last Modified: 2024-07-13
@Title : program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.

"""


def sort_list(Sample_list):

    """

    description:
        This function is used to sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.
    
    parameters:
        Sample_list(list) : list going to sort according to second value of tuple in list.
        
    return:
        none

    """


    sorted_list = sorted(Sample_list, key = lambda x: x[1])
    return sorted_list
        
    
    

def main():

    
    Sample_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

    sorted_tuples = sort_list(Sample_list)
    print(sorted_tuples)

    print("Sorted list of tuples by last element:", sorted_tuples)

if __name__ == "__main__":
    main()




