'''
@Author: Nagashree C R
@Date: 2024-07-13
@Last Modified by: Nagashree C R
@Last Modified: 2024-07-13
@Title : Program to print count of reversed strings in list.

'''


def no_of_reversed_strings(sample_list):

    """

    description:
        This function is used print count of reversed strings in list.
    
    parameters:
        sample_list(list) : list going to print count of reversed strings.
        
    return:
        none

    """

    count = 0

    for i in sample_list:
        if len(i)>=2:
            if i[::-1] == i:
                count+=1
    print(count)
    

def main():
 
    sample_list = ['abc', 'xyz', 'aba', '1221']
    no_of_reversed_strings(sample_list)


if __name__ == "__main__":
    main()