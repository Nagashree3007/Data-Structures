'''
@Author: Nagashree C R
@Date: 2024-07-12
@Last Modified by: Nagashree C R
@Last Modified: 2024-07-12 
@Title : Sorting dictionary value ascending order and descending order based on input
'''

def sort_dict_by_value(d, ascending=True):
    """
    Description: Function to sort the dictionary based on value 
    Parameter: 
        d, ascending=True : function taking parameters dictionary and bool value for sorting based on input
    Return:
       sorted_dict: returning the (ASC or DSC) sorted dictionary  
    """


    sorted_items = sorted(d.items(), key=lambda x: x[1], reverse=not ascending)
    sorted_dict = {k: v for k, v in sorted_items}

    return sorted_dict



example_dict = {'apple': 5, 'banana': 3, 'pear': 8, 'orange': 1}
sorted_dict_asc = sort_dict_by_value(example_dict, ascending=True)
print("Ascending order:", sorted_dict_asc)
sorted_dict_desc = sort_dict_by_value(example_dict, ascending=False)
print("Descending order:", sorted_dict_desc)