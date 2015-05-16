# Ian Garrett
# Lab4-2

def get_int(prompt_message):
    """(str) -> int
        displays prompt message,
        gets input from user
        converts input string to number,
        returns number to caller
    """
    prompt = prompt_message + ' '
    temp = input(prompt) # get input from user
    return int(temp)

limit = 10

do_again = 'y'
while do_again == 'y':
    x = get_int("Enter x as a number from -10 to 20")
    # is limit <x?
    if limit < x:
        print("Yes!", limit, "less than", x)
    else:
        print("No..", limit, "not less than", x)
    # is limit <=x?
    if limit <= x:
        print ("Yes!", limit,"less than or equal to", x)
    else: print("No..", limit,"not less than or equal to", x)
    # is limit == x?
    if limit == x:
        print ("Yes!", limit,"equal to", x)
    else:
        print ("No..", limit,"not equal to", x)
    # is is limit != x?
    if limit != x:
        print ("Yes!", limit,"not equal to", x)
    else:
        print ("No..", limit,"equal to", x)
    # loop will end when you type in an n
    do_again = input("try another? (y or n)")
# end while

