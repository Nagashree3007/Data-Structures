'''
@Author: Nagashree C R
@Date: 2024-07-12
@Last Modified by: Nagashree C R
@Last Modified: 2024-07-12  
@Title : Taking User input dictionary and iterating the key values pairs 
'''

def traversingDictionary():
    """
    Description : Function to take User input dictionary size,keys,values 
        and iterating the key values pairs using for loop 
    Parameter: 
    Return:
        dict1 : returning the concatinated new dictionary
    """

    
    size =int(input("Enter the size of the dictionary\n"))
    dict={}
    for i in range(size):
        key=input("Enter key : ")
        value=input(f"Enter value for key {key} = ")
        dict[key]=value
    return dict


dict=traversingDictionary()
for key, value in dict.items(): # items method returns key pairs 
    print(f"key : {key}--->value = {value}")
    