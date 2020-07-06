# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def check_even(n):
    """ checks if the number is even """
    remainder = n % 2
    return remainder == 0

def divisible_by_7(n):
    """ checks if number is divisible by 7 """
    remainder = n % 7
    return remainder == 0

names_and_ages = {'Demetri': 18, 'James': 28, 'Kat': 22, 'Maria': 28}

# for loop to iterate over the keys in the dictionary. 
for key in names_and_ages:
    # prints the value that corresponds with each key. 
    # Dictionary[key] -> value 
    print(names_and_ages[key])
    
for key in names_and_ages:
     # adds 1 to the values in the dictionary
    names_and_ages[key] = names_and_ages[key] + 1
    
# higher_order_function(function, list) -> new_list
    
# filters the even numbers from the number_list and then squares it
list(map(square, filter(check_even, number_list)))  