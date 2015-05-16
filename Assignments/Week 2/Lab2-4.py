# by Ian Garrett
# Lab2-4.py

def celsius_to_fahrenheit (celsius):
    '''Converts degrees in celsius to degrees in fahrenheit
    by multiplying degrees celsius by 9/5 and adding
    32 to the product.

    EXAMPLES:
    > celsius = 0 (freezing point)
    (0)*(9/5) + 32 = 32 fahrenheit freezing point

    > celsius = 100 (boiling point)
    (100)*(9/5) + 32 = 212 fahrenheit boiling point'''
    # Convert degrees in celsius to degrees in fahrenheit
    fahrenheit = ((celsius*float(9/5))+32)
    return fahrenheit

print (celsius_to_fahrenheit(100))

f = celsius_to_fahrenheit(34)
print (f)

print (celsius_to_fahrenheit(-40.0))
    
