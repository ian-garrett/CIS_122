# by Ian Garrett
# Lab5-1

print ("Tiny National Bank of Walterville\nCredit Card Payments")

reset = 'y'
while reset == 'y':
    account_balance = round(float(input("\nCredit card balance? ")),2)
    # insert if/elsif statement for returning payment due
    reset = input("\nAnother customer (y or n)? ")

def get_minpay():
    '''(input) -> float
takes credit card balance and returns appropriate payment

Examples:
Credit card balance? 100
Minimum payment due: $12.0

Credit card balance? 501
Minimum payment due: $13.53'''
    print ("Test")


