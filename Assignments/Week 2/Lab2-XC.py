# by Ian Garrett
# Lab 2-XC

import turtle
def draw_polygon(size, n_sides):
    # draws a polygon with side length "size" and n_sides
    for i in range (n_sides):
        turtle.forward(size)
        turtle.right(360/n_sides)
        # angle turned is determined by full circle(360)/number of sides
        
draw_polygon(50, 6)

def kelvin_to_fahrenheit(kelvin):
    # converts degrees in kelvin to degrees in fahrenheit
    fahrenheit = (float(9/5))*(kelvin - 273) + 32
    return fahrenheit

print (kelvin_to_fahrenheit(373.15))
# 373.15 is boiling point for K, so if this returns 212 all is well
    
