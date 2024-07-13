'''
@Author: Nagashree C R
@Date: 2024-07-12
@Last Modified by: Nagashree C R
@Last Modified: 2024-07-12   
@Title : To identify and print the unique values from the given list dictionary.
'''


def findUniqueValue(x):
    """
    Description : Function to iterating the every key value pair in the list dictionary 
    and every value adding into set this ensures the uniqueness 
    Parameter: 
        x: taking x as a list dictionary input into the function 
    Return:
        uniqueValue: returns the set formatted uniqe values
    """


    result=set()
    for val in dic:
        for value in val.values():
            result.add(value)
    return result    


dic= [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},{"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
res=findUniqueValue(dic)
print(res)


