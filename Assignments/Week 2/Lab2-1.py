# by Ian Garrett
# Lab2-1.py

import turtle
def draw_triangle (x):
    # Draw a triangle with side lengths x
    side_length = x
    for i in range (3):
        turtle.forward(side_length)
        turtle.right(120)
        # Draw and rotate line 3 times

draw_triangle(30)

x = 40
draw_triangle(x)

draw_triangle(x+20)

turtle.forward(60)
length = 60
for i in range(8):
    draw_triangle(length)
    length = length + 15


