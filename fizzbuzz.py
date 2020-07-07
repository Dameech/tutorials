# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 19:53:14 2020

@author: gramm
"""


# counting to 100. If number is divisible by 3, print fizz. if number is 
# divisible by 5, print buzz. if number is divisible by both, print fizzbuzz.
# otherwise print the number

# 






list_1 = list(range(1, 100))
for number in list_1:
    if 0 == number % 15:
        print("fizzbuzz")
    elif 0 == number % 5:
        print("buzz")
    elif 0 == number % 3:
        print("fizz")
    else:
        print(number)