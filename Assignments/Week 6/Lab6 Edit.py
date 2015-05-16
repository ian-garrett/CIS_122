# by Ian Garrett
# Lab 6

# Functions

def circle_area(radius):
    '''((float)->float
    returns area of circle based on input radius
    circle_area(1)
    >pi'''
    pi = 3.141592
    area = (radius*radius*pi)
    return area

def cylinder_volume(radius, height):
    '''(float->float
    returns volume of cylinder based on input radius and height
    cylinder_volume(1,1)
    >pi'''
    pi = 3.141592
    volume = (radius*radius*height*pi)
    return volume

def get_float(amount):
    '''(number)->float #how should I label input? int? number?
    takes amount and returns amount as a float
    get_float(10)
    >10.0'''
    return float(amount)

def square_number(number):
    '''((float)->float
    returns number squared
    square(4.0):
    >16'''
    square = (number*number)
    return square        
        

def swap_case(string):
    '''()->str
    returns input as string with cases switched
    swap_case("Bat")
    >bAT'''
    return string.swapcase()

def evaluate_mood():
    '''()->float
    Returns an appropriate message based on user input between 0-10'''
    scale = float(input("On a scale of 0 to 10, how is your day going? (# 1-10) "))
    while scale > 10 or scale <0:
        scale = float(input("\nInvalid number. Please a number inbetween 1 and 10 "))
    if 0 <= scale <4:
        return  ("\nKeep your chin up")
    elif 4 <= scale < 7:
        return  ("\nTry to find the simple pleasures of the average day")
    elif 7 <= scale <= 10:
        return ("\nMay you have many more glorious days like this one")
    

# Main Program

def main_program():
    '''Runs functions and prints statements using outputs of functions'''
    print ("\nCalculating the area of an circle")
    area = round(circle_area(float(input("Enter radius "))),2)
    print ("\nArea of circle is ", area,"units^2")

    print ("\nCalculating volume of a cylinder")
    radius = (float(input("Enter radius ")))
    height = (float(input("Enter height ")))
    volume = round(cylinder_volume(radius, height), 2)
    print ("\nVolume of cylinder is ", volume,"units^3")

    print ("\nConverting number to float")
    number_float = get_float(input("Enter numerical amount "))
    print  ("\nFloat amount is", number_float)

    print ("\nSquaring a number")
    input_number =  float(input("Enter number "))
    number =square_number(input_number)
    print ("\nSquare of", input_number, " is ", number)

    print ("\nSwitching characters of a string")
    swap = str.swapcase(str(input("Enter string (characters, mixed cases [EXAMPLE: HeLLo]) ")))
    print ("\nString with swapped charactors is ", swap)

    print ("\nEvaluating emotion and responding appropriately")
    mood = evaluate_mood()
    print (mood)

# While function

def get_ok():
    '''() -> str
    returns "y" or "n" from user input
    re_run = re_run.lower() # make lower case'''
    re_run  =  "y"
    print ("Welcome to my program")
    while re_run ==  "y":
        main_program()
        re_run = input("\nRun program again? (y/n): ")
        if re_run == "n":
             print ("\nThank you for using my program")

# Run main program

get_ok()
