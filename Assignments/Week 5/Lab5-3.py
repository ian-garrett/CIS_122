# by Ian Garrett
# Lab5-3

print ("Tiny National Bank of Walterville\nCredit Card Payments")

def get_minpay(balance, percent, min_amnt):
    ''' float -> round.float -> string
takes balance and calculates the appropriate payment due.

Examples:
Credit card balance? 100
Minimum payment due: $12.0

Credit card balance? 501
Minimum payment due: $13.53'''
    rounded_balance = round(balance, 2)
    balance_due = round((balance*percent), 2)
    if 0 < balance <= min_amnt:
        return rounded_balance
    elif min_amnt < balance <= 100:
        return min_amnt
    else:
        return balance_due
        
reset = 'y'
while reset == 'y':
    balance = float(input("\nCredit card balance? "))
    if  get_minpay(balance, .027, 12.00) <= 0:
        print ("Your balance is current, no payment is needed")
    else:
        print ("Minimum payment due: $", (get_minpay(balance, .027, 12.00)))
    reset = input("\nAnother customer (y or n)? ")

# Tested with given values
#Tiny National Bank of Walterville
#Credit Card Payments
#
#Credit card balance? 100
#Minimum payment due: $12.0
#
#Another customer (y or n)? y
#
#Credit card balance? 501
#Minimum payment due: $13.53
#
#Another customer (y or n)? y
#
#Credit card balance? 8.97
#Minimum payment due: $8.97
#
#Another customer (y or n)? y
#
#Credit card balance? 0
#Your balance is current, no payment is needed
#
#Another customer (y or n)? n
