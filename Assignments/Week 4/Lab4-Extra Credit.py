# Ian Garrett
# Lab4-Extra Credit

reset = "y"
while reset == "y":
    income = float((input("Please enter yearly income: ")))
    if income < 15000:
        rate = .005
    elif 15000 < income <= 17500:
        rate = .006
    elif 17500 < income <= 22400:
        rate = .01
    elif 22400 < income <= 47300:
        rate = .014
    elif 47300 < income <= 75000:
        rate = .018
    elif 75000 < income <= 112450:
        rate = .022
    elif 112450 < income <= 277000:
        rate = .027
    else:
        rate = .03
    print ("Yearly Income: ", income, "Tax Rate: ", rate, "Tax Due: ", (income*rate))
    reset = input("Calculate another tax rate? (y or n): ")
                      


