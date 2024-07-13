'''
@Author: Nagashree C R
@Date: 2024-07-12
@Last Modified by: Nagashree C R
@Last Modified: 2024-07-12
@Title : program to print out a set containing all the colors from color_list_1 which
are not present in color_list_2.
'''

color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])

color_list_1 = list(color_list_1)
color_list_2 = list(color_list_2)

print(color_list_2)

result_set=[]

for i in color_list_1:
    if i not in color_list_2 :
        result_set.append(i)
print(set(result_set))
