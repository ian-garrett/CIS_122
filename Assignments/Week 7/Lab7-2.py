# by Ian Garrett'
# Lab 7-2

# In saving pictures, I decided to also append the color and bg color of the image to the favorites list

print ("Welcome to my turtle program\n")

import turtle

turtle.speed(0)

def draw_picture(angle, number_of_lines, color, bgcolor):
    for i in range (number_of_lines):
        turtle.color(color)
        turtle.bgcolor(bgcolor)
        turtle.forward(100)
        turtle.right(angle)

def get_ok():
    ok = input("Do again? Press y or n ")
    ok = ok.lower() + "x"
    ok = ok[0]
    return ok

def ask_y_or_n(question):
    answer = ' '
    while answer != 'y' and answer != 'n':
        answer = input (question + "'Press y or n ")
        answer = answer .lower() + "x"
        answer = answer[0]
    return answer

def get_float(prompt):
          temp = input(prompt + ' ')
          return float(temp)

def get_int(prompt):
          temp = input(prompt + ' ')
          return int(temp)

def get_str(prompt):
    temp = input(prompt + ' ')
    return str(temp)
    

favorites = list()

rerun = 'y'
while rerun == 'y':
    turtle.reset()
    color = get_str("Enter line color ")
    bg_color = get_str("Enter background color ")
    angle = get_float("Enter angle to turn ")
    number_of_lines = get_int("Enter number of lines ")
    for i in range (number_of_lines):
            turtle.color(color)
            turtle.bgcolor(bg_color)
            turtle.forward(100)
            turtle.right(angle)
    save = ask_y_or_n("\nWould you like to add this picture to your list of favorites? ")
    if save == "y":
        favorites.append([angle, number_of_lines, color, bg_color])
    turtle.bgcolor("white")
    rerun = ask_y_or_n("\nWould you like to create another picture? ")      

print ("\nFavorite Pictures:")
picture_number = 1
for favorite in favorites:
    print ("\nPicture number ", picture_number,"\nAngle: ", favorite[0], "degrees",  "\nNumber of lines: ", favorite[1], "\nColor: ", favorite[2], "\nBackground color: ", favorite[3])
    draw_picture(favorite[0], favorite[1], favorite[2], favorite [3])
    picture_number += 1

print ("Exiting program...")
        

    
    
    
