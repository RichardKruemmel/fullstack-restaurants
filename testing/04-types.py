#!/usr/bin/env python3

""" 
The fourth file in a series to learn about how testing works.

In this example, we will check if the correct types are being passed into a function
"""


def multiply_two_numbers(x, y):
    return x*y    

print(multiply_two_numbers(2, 3))
print(multiply_two_numbers(3,"ha"))
