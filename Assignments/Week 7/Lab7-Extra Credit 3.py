# by Ian Garrett
# Lab 7-Extra Credit 3

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

size = 40

repeat = 0

turtle.begin_fill()
while repeat != 40:
    turtle.fillcolor(color_1)
    draw_polygon((size), 5)
    color_1,color_2 = color_2,color_1 # common way to swap variables over iterations
    size += 3
    turtle.right(20)
    invis_move(20)
    repeat += 1
turtle.end_fill()
