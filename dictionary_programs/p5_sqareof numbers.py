'''
@Author: Nagashree C R
@Date: 2024-07-12
@Last Modified by: Nagashree C R
@Last Modified: 2024-07-12  
@Title : Python script to generate and print a dictionary that contains a
number (between 1 and n) in the form (x, x*x).
'''


def do_dictionary(n):
    """
    Description : Function to stores the key, and value is key*key and print the dictionary 
    Parameter: Function taking the n as a user input parameter
    Return:
        dict1 : returning the concatinated new dictionary
    """


    dic={}
    for i in range(1,n+1):
        key=i
        value=i*i
        dic[key]=value
    return dic
    


n=int(input("Enter the value of N\n"))
res=do_dictionary(n)
print(res)