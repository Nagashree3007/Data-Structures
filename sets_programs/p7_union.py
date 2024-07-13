"""

@Author: Nagashree C R
@Date: 2024-07-13
@Last Modified by: Nagashree C R
@Last Modified: 2024-07-13 
@Title : Program to create an union of set.

"""

def union_set(numbers1, numbers2):

    """

    description:
        This function is used create an union of set.
    
    parameters:
        numbers1, numbers2(set) : sets that are going to print union elements.
        
    return:
        none

    """
    # for i in numbers2:
    #     numbers1.add(i)
    # print(numbers1)

    print(numbers1.union(numbers2))  

def main():
    numbers1 = {1, 2, 3, 4, 5}
    numbers2 = {2, 3, 4}
    union_set(numbers1, numbers2)


if __name__ == "__main__":
    main()