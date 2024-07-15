'''
@Author: Nagashree C R
@Date: 2024-07-12
@Last Modified by: Nagashree C R
@Last Modified: 2024-07-12
@Title :program to access environment variables.
'''

import os

def access_environment_variables():
    """ Access and print environment variables """
    # Accessing specific environment variables
    home_dir = os.environ.get('USERPROFILE')
    python_path = os.environ.get('PYTHONPATH')

    # Print environment variables
    print(f"HOME: {home_dir}")
    print(f"PYTHONPATH: {python_path}")

    # Print all environment variables
    print("\nAll environment variables:")
    for key, value in os.environ.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    access_environment_variables()
