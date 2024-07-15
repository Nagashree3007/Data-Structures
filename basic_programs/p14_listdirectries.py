'''
@Author: Nagashree C R
@Date: 2024-07-12
@Last Modified by: Nagashree C R
@Last Modified: 2024-07-12
@Title : program to list all files in a directory in Python.
'''

import os

def list_files(directory):
    if os.path.isdir(directory):
        print(f"Listing files in directory: {directory}")
        files = os.listdir(directory)
        for file in files:
            print(file)
    else:
        print(f"Error: {directory} is not a valid directory")

if __name__ == "__main__":
    directory_path = input("Enter the directory path: ").strip()
    list_files(directory_path)
