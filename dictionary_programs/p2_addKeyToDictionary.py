'''
@Author: Nagashree C R
@Date: 2024-07-12
@Last Modified by: Nagashree C R
@Last Modified: 2024-07-12  
@Title : Taking user input as a key value pairs and store it into a dictionary
'''

def addDictionary(dict):
    """
    Description: Function to store the user inputs key value pairs
    Parameter: 
        d, ascending=True : function taking parameters dictionary and bool value for sorting based on input
    Return:
       sorted_dict: returning the (ASC or DSC) sorted dictionary  
    """


    size =int(input("Enter the size of the key-value pairs u want to add dictionary\n"))
    for i in range(size):
        key=input(f"Enter key : ")
        value=int(input(f"Enter value for key {key} = "))
        dict[key]=value
    return dict
dic={0: 10, 1: 20}
d1=addDictionary(dic)
print(d1)

