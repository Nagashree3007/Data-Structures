'''
@Author: Nagashree C R
@Date: 2024-07-12
@Last Modified by: Nagashree C R
@Last Modified: 2024-07-12 
@Title : Python program to check multiple keys exists in a dictionary.
'''


'''def checkKeys(my_dict):
    """
    Description: Function to check wether multiples keys present in the dictionary or not
    Parameter: 
        keys, my_dict : Function taking keys and dictionary as a input
    Return:
       True or False : returning the bool value based on the key presence
    """
    result=[]
    for item in my_dict:
        for key in my_dict.keys():
            result.append(key)
    return result
    
def checkTorF(x,user_dic):
    for i in x:
        for key in user_dic.keys():
            if x==key:
                return True
    return False
    '''
def checkTorF(my_dict,user_dic):
    for i in my_dict.keys():
        for key in user_dic.keys():
            if i==key:
                return True
    return False


my_dict = {'1': 'Alice','2':'jaya'}
user_dic= {'3': 'Alice','4':'jaya'}
#x=checkKeys(my_dict,user_dic)
#y=checkTorF(x,user_dic)
y=checkTorF(my_dict,user_dic)
print(f"In the given dictionary is the multiple key exits. .???: {y}")
