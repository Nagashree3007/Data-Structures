'''
@Author: Nagashree C R
@Date: 2024-07-12
@Last Modified by: Nagashree C R
@Last Modified: 2024-07-12
@Title :create a histogram from a given list of integers.
'''

def create_histogram(numbers):
    histogram = {}
    
    # Count frequency of each number
    for num in numbers:
        if num in histogram.keys():
            histogram[num] += 1
        else:
            histogram[num] = 1
    
    # Print histogram
    for key,val in sorted(histogram.items()):
        print(f"{key}: {'*' * val}")

# Example usage:
numbers = [1, 2, 1, 3, 2, 1, 4, 2, 1, 5]
create_histogram(numbers)
