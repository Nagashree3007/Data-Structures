"""

@Author: TarunSai
@Date: 2024-07-04
@Last Modified by: 
@Last Modified time:
@Title : Program to find the list of words that are longer than n from a list.

"""


def find_long_words(list_of_strings, n):

    """

    description:
        This function is used give list of words that are greater than n.
    
    parameters:
        list_of_strings(list) : numbers in a list going to print in the function.
        
    return:
        none

    """
    
    for i in list_of_strings:
        if len(i)>n:
            print(i)


def main():


    n = int(input("enter n value: "))
    list_of_strings = ['tarun', 'varun', 'hello', 'python']
    find_long_words(list_of_strings, n)


if __name__ == "__main__":
    main()