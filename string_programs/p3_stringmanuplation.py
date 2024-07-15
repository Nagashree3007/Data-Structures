"""

@Author: Nagashree C R
@Date: 2024-07-13
@Last Modified by: Nagashree C R
@Last Modified: 2024-07-13
@Title : Program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.

"""


def modify_string(string):

    """

    description:
        This function is used to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
    
    parameters:
        string(str) : string that is going to modify
        
    return:
        none

    """

    first_char = string[0]
    modified_str = first_char
    for i in string[1::]:
        if i == first_char:            
                modified_str += '$'
        else:
             modified_str += i
    print(modified_str) 
    
    



def main():

    string = input("enter a string: ")
    modify_string(string)


if __name__ == "__main__":
    main()