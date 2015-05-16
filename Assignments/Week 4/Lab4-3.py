# Ian Garrett
# Lab4-3

def get_float(prompt_message):
    """(str) -> float
        displays prompt message,
        gets input from user
        converts input string to float number,
        returns number to caller
    """
    prompt = prompt_message + ' '
    temp = input(prompt) # get input from user
    return float(temp)

limit = 10

do_again = 'y'
while do_again == 'y':
    x = get_float("Enter x as a price from $-10.00 to $20.00(no $ sign):")
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

# Results (4.37):
#   No.. 10 not less than 4.37
#   No.. 10 not less than or equal to 4.37
#   No.. 10 not equal to 4.37
#   Yes! 10 not equal to 4.37

