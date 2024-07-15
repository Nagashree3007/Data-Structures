"""

@Author: TarunSai
@Date: 2024-07-04
@Last Modified by: 
@Last Modified time:
@Title : Program to split a list based on first character of word.

"""


def split_list(list_of_items):

    """

    description:
        This function is used to split a list based on first character of word.

    parameters:
        list_of_items(list) : list of elements.
        
    return:
        none

    """

    dict_items = {}

    for i in list_of_items:
        
        first_char = i[0]

        if first_char in dict_items:
            dict_items[first_char].append(i)
        else:
            dict_items[first_char] = [i]
    
    print(dict_items)

def main():

    list_of_items = eval(input("enter a input list: "))
    split_list(list_of_items)
    


if __name__ == "__main__":
    main()