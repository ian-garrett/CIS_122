# Ian Garrett
# Lab4-6

do_again = 'y'
while do_again == 'y':
    x = int (input("Enter total points here: "))
    # is grade a S?
    if 50 <= x:
        print(x, "S")
    # is grade an A?
    elif 40 <= x < 50:
        print (x, "A")
    # is grade a B?
    elif 30 <= x < 40:
        print (x, "B")
    # is grade a C?
    elif 25 <= x < 30:
        print (x, "C")
    # is grade a Z?
    else:
        print (x, "Z")

    # loop will end when you type in an n
    do_again = input("try another? (y or n): ")
# end while


