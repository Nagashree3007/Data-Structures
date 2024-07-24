'''

@Author: Nagashree C R
@Date: 2024-07-12
@Last Modified by: Nagashree C R
@Last Modified: 2024-07-12
@Title : Creating and iterating array elements

'''

import os

import loggingfile

current_scriptname=os.path.basename(__file__)

logger=loggingfile.logg(current_scriptname)

array_of_integers = [10, 20, 30, 40, 50]
logger.info("Elements of the array based on index:")
for i in range(len(array_of_integers)):
    logger.info(f"Element at index {i} = {array_of_integers[i]}")







