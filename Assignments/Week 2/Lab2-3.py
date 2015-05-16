# by Ian Garrett
# Lab2-3.py

import turtle
def draw_triangle (x):
    '''Draws an equilateral triangle by
    moving forward x and turning 60 degrees to the right.
    Input x is equal to the desired side length.'''
    # Draw a triangle with side lengths x
    side_length = x
    for i in range (3):
        turtle.forward(side_length)
        turtle.right(120)
        # Draw and rotate line 3 times
help(draw_triangle)
