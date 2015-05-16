# Ian Garrett
# Lab4-7

reset = "y"

age = int(input("Enter age: "))
BMI = float(input("Enter BMI: "))

young = age < 45
slim = BMI < 0.22


while reset == "y":
    if young and slim:
        risk = "Low"
    elif young and not slim:
        risk = "Moderate"
    elif not young and slim:
        risk = ("Moderate")
    else:
        risk = ("High")
    print ("Age: ", age, "BMI: ", BMI,"Risk Level: ", risk)
    reset = input("Continue to new test? (y or n): ")
# end while




         


