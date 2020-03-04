#!/usr/bin/env python3

""" 
The third file in a series to learn about how testing works.

In this example, we will use assert to check if a variable is found in a predefined list.
"""

colors = ["red", "green", "blue"]

def get_favorite_color():
    """A function to ask the user what their favorite color is"""
    favorite_color = input("What is your favorite color? ")
    
    # check if the color is in our list
    assert favorite_color in colors
    
print(get_favorite_color())