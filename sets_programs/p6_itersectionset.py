"""

@Author: Nagashree C R
@Date: 2024-07-13
@Last Modified by: Nagashree C R
@Last Modified: 2024-07-13 
@Title : Program to create an intersection of set.

"""

def itersection_set(numbers1, numbers2):

    """

    description:
        This function is used create an intersection of set.
    
    parameters:
        numbers1, numbers2(set) : sets that are going to print intersection elements.
        
    return:
        none

    """
    numbers = set()
    # for i in numbers1:
    #     for j in numbers2:
    #         if i==j:
    #             numbers.add(i)  
    # print(numbers) 
    print(numbers1.intersection(numbers2))       

def main():
    numbers1 = {1, 2, 3, 4, 5}
    numbers2 = {2, 3, 4}
    itersection_set(numbers1, numbers2)


if __name__ == "__main__":
    main()