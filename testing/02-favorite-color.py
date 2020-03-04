#!/usr/bin/env python3

""" 
The second file in a series to learn about how testing works.

In this example, we will use assert
"""

colors = ["red", "green", "blue"]

def get_favorite_color():
    """A function to ask the user what their favorite color is"""
    favorite_color = input("What is your favorite color? ")
    
    # check if the color is in our list
    if favorite_color not in colors:
        print("Sorry, that isn't one of our colors")
        return 0
    else: 
        return favorite_color

print(get_favorite_color())