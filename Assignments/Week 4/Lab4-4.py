# Ian Garrett
# Lab4-4

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

#Results
# 'A'
#   No.. argon not less than A
#   No.. argon not less than or equal to A
#   No.. argon not equal to A
#   Yes! argon not equal to A
# 'a'
#   No.. argon not less than a
#   No.. argon not less than or equal to a
#   No.. argon not equal to a
#   Yes! argon not equal to a
# 'Aster'
#   No.. argon not less than Aster
#   No.. argon not less than or equal to Aster
#   No.. argon not equal to Aster
#   Yes! argon not equal to Aster
# 'Z'
#   No.. argon not less than Z
#   No.. argon not less than or equal to Z
#   No.. argon not equal to Z
#   Yes! argon not equal to Z
