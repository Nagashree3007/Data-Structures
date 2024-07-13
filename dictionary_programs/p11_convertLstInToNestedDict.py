'''
@Author: Nagashree C R
@Date: 2024-07-12
@Last Modified by: Nagashree C R
@Last Modified: 2024-07-12 
@title:Python program to convert a list into a nested dictionary of keys.
'''

def list_to_nested_dict(keys_list, value):
    """
    Convert a list into a nested dictionary of keys with a common value.
    
    Parameters:
    keys_list (list): List of keys to be converted into nested dictionaries.
    value: Value to be assigned at the innermost level of the nested dictionary.
    
    Returns:
    dict: Nested dictionary created from the list of keys.
    """


    result = {}
    current_dict = result
    
    for key in keys_list[:-1]:
        current_dict[key] = {}
        current_dict = current_dict[key]
    
    current_dict[keys_list[-1]] = value
    
    return result

keys_list = ['A', 'B', 'C']
value = 10

nested_dict = list_to_nested_dict(keys_list, value)
print("Nested Dictionary:")
print(nested_dict)
