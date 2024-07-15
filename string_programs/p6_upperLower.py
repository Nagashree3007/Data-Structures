"""

@Author: Nagashree C R
@Date: 2024-07-15
@Last Modified by: Nagashree C R
@Last Modified: 2024-07-15
@Title : Program script that takes input from the user and displays that input back in uppercase and lowercase.

"""


def case_string(string):

    """

    description:
        This function is used upper and lower cases uppercase and lowercase.  

    parameters:
        string(str) : string going to convert uppercase and lowercase.
        
    return:
        none

    """

    lower_case = string.lower()
    upper_case = string.upper()
    print(f'lowercase = {lower_case}')
    print(f'upper_case = {upper_case}')    

    
def main():

    global string
    string = input("enter a string: ")
    case_string(string)

if __name__ == "__main__":
    main()