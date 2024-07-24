'''

@Author: Nagashree C R
@Date: 2024-07-12
@Last Modified by: Nagashree C R
@Last Modified: 2024-07-12 
@Title : Reverse the order of items in the Array


'''


import os

import loggingfile

current_scriptname=os.path.basename(__file__)

logger=loggingfile.logg(current_scriptname)

array_of_integers = [10, 20, 60 , 40, 50]

logger.info("Original array:--->{}".format(array_of_integers))

#for reversing the elements
reversed_array = array_of_integers[::-1]
array2_integers =reversed_array

logger.info("Reversed array:---> {}".format( array2_integers ))