# Ian Garrett
# Lab4-5

element = "argon"

do_again = 'y'
while do_again == 'y':
    x = input("Enter characters here: ")
    # is 'argon' <x?
    if element < x:
        print("Yes!", element, "less than", x)
    else:
        print("No..", element, "not less than", x)
    # is 'argon' <=x?
    if element <= x:
        print ("Yes!", element,"less than or equal to", x)
    else: print("No..", element,"not less than or equal to", x)
    # is 'argon' == x?
    if element == x:
        print ("Yes!", element,"equal to", x)
    else:
        print ("No..", element,"not equal to", x)
    # is is 'argon' != x?
    if element != x:
        print ("Yes!", element,"not equal to", x)
    else:
        print ("No..", element,"equal to", x)
    # loop will end when you type in an n
    do_again = input("try another? (y or n)")
# end while

# Results (14):
#   No.. argon not less than 14
#   No.. argon not less than or equal to 14
#   No.. argon not equal to 14
#   Yes! argon not equal to 14
