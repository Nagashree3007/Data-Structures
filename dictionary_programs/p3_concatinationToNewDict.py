'''
@Author: Nagashree C R
@Date: 2024-07-12
@Last Modified by: Nagashree C R
@Last Modified: 2024-07-12   
@Title : Concatinating the given dictionaries in to a new dictionary
'''

def concateToDictionary(dic1,dic2,dic3):
    """
    Description: Function to store the user inputs dictionaries into dictionary
    Parameter: 
    dic1,dic2,dic3, : taking three individual dictionaries
    Return:
    result_dict : returning the concatinated new dictionary
    """


    result_dict = {**dic1, **dic2, **dic3}
    print(result_dict)



dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}

concateToDictionary(dic1,dic2,dic3)












