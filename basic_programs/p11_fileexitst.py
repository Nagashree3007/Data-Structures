'''
@Author: Nagashree C R
@Date: 2024-07-12
@Last Modified by: Nagashree C R
@Last Modified: 2024-07-12
@Title :program to check whether a file exists.
'''

import os

def check_file_exists(file_path):
    return os.path.exists(file_path)

file_path = 'c:/Users/ASHAY/OneDrive/Desktop/bridgelabz/basic_program/p9_histogram.py'

if check_file_exists(file_path):
    print(f"The file '{file_path}' exists.")
else:
    print(f"The file '{file_path}' does not exist.")
