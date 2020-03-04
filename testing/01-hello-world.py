#!/usr/bin/env python3

""" 
The first file in a series to learn about how testing works. 

This example looks at a function which is expected to return a simple string.
"""

def hello_world():
    """Function that returns something that we expect"""
    return ""

if hello_world()=="Hello, World":
    print("function works as expected")
else:
    print("Error.")

# print(hello_world())
