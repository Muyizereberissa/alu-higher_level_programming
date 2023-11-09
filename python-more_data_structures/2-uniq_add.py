#!/usr/bin/python3
def uniq_add(my_list=[]):
    # Use a set to store unique integers
    unique_integers = set()
    
    # Iterate through the list
    for num in my_list:
        # Add the integer to the set
        unique_integers.add(num)
    
    # Calculate the sum of unique integers
    result = sum(unique_integers)
    
    return result    
