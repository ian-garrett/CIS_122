# by Ian Garrett'
# Lab 7-1

print ("Welcome to my turtle program\n")

import turtle

turtle.speed(0)

def get_ok():
    ok = input("Do again? Press y or n")
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
          temp = input(prompt + '  ')
          return int(temp)

def get_str(prompt):
    temp = input(prompt + ' ')
    return str(temp)


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
    rerun = "n"

print ("Exiting program...")
    
    
    
    
