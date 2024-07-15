'''
@Author: Nagashree C R
@Date: 2024-07-12
@Last Modified by: Nagashree C R
@Last Modified: 2024-07-12
@Title : to print the documents (syntax, description etc.) of Python built-in
function(s).
'''


def print_doc(function_name):
    print(f"Documentation for {function_name}:")
    help(function_name)


print_doc(abs)
