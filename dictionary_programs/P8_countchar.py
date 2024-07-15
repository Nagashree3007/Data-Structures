'''
@Author: Nagashree C R
@Date: 2024-07-12
@Last Modified by: Nagashree C R
@Last Modified: 2024-07-12 
@Title : count the occurance of each char in the sentence 
'''
sentence='w3resource'
def counting(sentence):
    """
    Description: Function to find the occurance of char in the sentence given
    Parameter: 
        sentence-which the suer want to count
    Return:
       d: dictionary that shows the char occurance of a sentence
    """

    d={}
    for i in sentence:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    return d
d=counting(sentence)
for key,val in sorted(d.items()):
    print(f'{key}--->{val}',end=',')
print('\n')
for key,val in sorted(d.items(),key=lambda x:x[1],reverse=True):
    print(f'{key}--->{val}',end=',')
print('\n')
for key,val in sorted(d.items(),key=lambda x:x[1]):
    print(f'{key}--->{val}',end=',')
print('\n')