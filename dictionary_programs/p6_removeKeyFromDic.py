'''
@Author: Nagashree C R
@Date: 2024-07-12
@Last Modified by: Nagashree C R
@Last Modified: 2024-07-12  
@Title : To remove a particular key from dictionary.
'''



def removeDictionaryKey(size):
    """
    Description : Function to taking User input as a dictionary size and create the dictionary
    based on incoming parameter 
    Parameter: 
        size: taking size as a input parameter for creating dictionary 
    Return:
    """


    dict1={}
    for i in range(size):
        key=int(input(f"Enter key : "))
        value=input(f"Enter value for key {key} = ")
        dict1[key]=value

    print("*** Before deleting the key*** ",dict1)
    key=int(input("Enter the key for which key value you want to be deleting : \n"))
    del dict1[key]
    print("*** After deleting the key*** ",dict1)


size =int(input("Enter the size of the dictionary :\n"))
removeDictionaryKey(size)