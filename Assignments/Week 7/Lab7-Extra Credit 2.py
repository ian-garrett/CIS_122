# by Ian Garrett
# Lab 7-Extra Credit 2

import turtle

turtle.speed(0)

def draw_polygon(length, n_sides):
    angle = 360 / n_sides
    for i in range (n_sides):
        turtle.forward(length)
        turtle.right(angle)

def invis_move(distance):
    turtle.penup()
    turtle.forward(distance)
    turtle.pendown()
    
        
color_1 = "red"
color_2 = "blue"

size = 150

repeat = 0

while repeat != 32:
    turtle.fillcolor(color_1)
    turtle.begin_fill()
    draw_polygon((size), 6)
    turtle.end_fill()
    color_1,color_2 = color_2,color_1 # common way to swap variables over iterations
    size -= 4
    turtle.right(5)
    invis_move(5)
    repeat += 1
    
    
    
    
