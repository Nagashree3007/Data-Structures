"""

@Author: Nagashree C R
@Date: 2024-07-15
@Last Modified by: Nagashree C R
@Last Modified: 2024-07-15
@Title : Program to reverse of a string.

"""


def reverse_string(string):

    """

    description:
        This function is used to reverse of a string.
    
    parameters:
        string(str) : string that going to reverse
        
    return:
        none

    """

    print(string[::-1], "is the reverse of string") 

def main():

    string = input("enter a string: ")
    reverse_string(string)


if __name__ == "__main__":
    main()