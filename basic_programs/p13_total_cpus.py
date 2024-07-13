'''
@Author: Nagashree C R
@Date: 2024-07-12
@Last Modified by: Nagashree C R
@Last Modified: 2024-07-12
@Title : program to find out the number of CPUs using.
'''

import os
cpus=os.cpu_count()
print(f'total number of CPU\'s are {cpus}')
