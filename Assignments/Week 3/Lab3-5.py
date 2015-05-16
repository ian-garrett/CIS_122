# Ian Garrett
# Lab3-5

price = input("Enter the price: ")
# Packaged input code from Lab3-4

def get_float(prompt):
    prompt = float(prompt)
    # Labels prompt as a float, multiplies prompt by 2, rounds product to 2 decimal places
    prompt *=2
    prompt = round(prompt, 2)
    print (prompt)
    # Could have been condenced into "print (round((float(prompt)*2),2))"

get_float(price)

