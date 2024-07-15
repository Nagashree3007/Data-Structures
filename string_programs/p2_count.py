"""

@Author: Nagashree C R
@Date: 2024-07-13
@Last Modified by: Nagashree C R
@Last Modified: 2024-07-13
@Title : Program to count the number of characters (character frequency) in a string.

"""


def char_frequency(string):

    """

    description:
        This function is used to count the number of characters (character frequency) in a string.
    
    parameters:
        string(str) : string that going to count character frequency.
        
    return:
        none

    """

    char_frequency = {}

    for i in string:
        
        if i in char_frequency:
            char_frequency[i] += 1
        else:
            char_frequency[i] = 1
    
    print(char_frequency)

def main():

    string = 'google.com'
    char_frequency(string)


if __name__ == "__main__":
    main()