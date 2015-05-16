# by Ian Garrett
# Lab 8/Lab 8-Extra Credit

# NOTES:
# 1) Both parts of the extra credits are included.
# 2) Due to IDLE's strange formatting, "." is not displayed as the same length as a normal charactor or
#         an " ".  For this reason I used " "(empty space)  as the pad_char for my fixed_width functions in order
#         to fulfil the extra credit requirements.
# 3) The way that the code shown in the lab 8 assignment .pdf operates, the program proceeds to cancel
#         the order and in turn terminates itself as long as the input is anything besides "Shop" or "Checkout".
#         This is problematic, as the program shuts down without explanation if the user enters shop or checkout
#         incorrectly for any reason. I used an if statement to correct this, providing the user with the feedback
#         that they entered an invalid response and prompting them for another answer via user input. To make
#         this if statement callable if the proceeding responses do not match one of the three actions provided, I
#         had to package the 1 while and 3 if statements within another while statement, the conditions of which
#         were violated through assignment at the end of the "Checkout" and "Cancel", calling the final print
#         statements and ending the program.

# Lists
products = ["Turkey", "Cranberry", "Pumpkin Pie", "Spicy Latte", "Yams"]
prices = [26.95, 3.95, 8.95, 4.95, 1.99]
cartQty = [0, 0, 0, 0, 0]
product_numbers = [1, 2, 3, 4, 5]

# Functions

# EXTRA CREDIT 1
def fixed_width(item, width, pad_char):
          '''(str, int, str) -> str
          returns item in a fixed width string ending in pad_char's
          '''
          n = len(item)
          pad_len = width - n
          fixed_width_item = item + (pad_len * pad_char)
          return fixed_width_item

def display_products(products, prices):
          '''(list, list) -> None
          Display a list of products and prices
          '''
          print()
          print ("ShopMart's Thanksgiving Specials:")
          fw_desc = fixed_width("Description", 16, " ")
          print (fixed_width("#", 5, " ") + fw_desc + "\tPrice")
          product_num = 1
          repeat_num = 0
          for i in products:
                    fw_num = fixed_width(str(product_num), 5, " ")
                    fw_descr = fixed_width(products[repeat_num], 16, "  ")
                    print (fw_num, fw_descr,  "\t", prices[repeat_num])
                    product_num += 1
                    repeat_num += 1

def display_cart(cartQty, products, prices):
          '''list -> None
          Displays shopping cart's products, prices, and quantities
          '''
          print()
          print ("Shopping cart contents:")
          fw_item = fixed_width("Item", 14, " ")
          print (fixed_width("Qty", 7, " ") + fw_item + "\tPrice","\tSubtotal")
          item_num = 0
          amount_owed = 0
          for i in cartQty:
                    if i != 0:
                              subtotal= int(i)*prices[item_num]
                              fw_Qty = fixed_width(str(i), 5, " ")
                              fw_product = fixed_width(products[item_num], 14, " ")
                              fw_price = fixed_width(str(prices[item_num]) , 5, " ")
                              print ((" "*5 + fw_Qty), fw_product,"\t", fw_price,"\t", format(subtotal, ".2f")) # EXTRA CREDIT 2
                              item_num += 1
                              amount_owed += subtotal
                    else:
                              item_num += 1
          
          print ("Your cart total is","\t", fixed_width("$", 14, " "),"\t", format(amount_owed, ".2f"))  # EXTRA CREDIT 2

def shop(user_input):
          '''(float) -> none
          Prompts users to add items to there cart, which is the list "cartQty"
          '''
          display_products(products, prices)
          item_select = int(input("Product number: "))
          cartQty[(item_select)-1]  += 1
          print ("You added ", products[item_select], "to your cart for", "$", prices[item_select])         


# Program
print("Welcome to Shopmart's exclusive Thanksgiving specials")
print()

total_owed = 0

action = str.capitalize(input("Action: Shop, Cancel, Checkout? "))

end_program = "not yet"
while end_program != "end":
          if action != "Shop" and action != "Cancel" and action != "Checkout":
                    # This if statement prevents entering something
                    # spelled incorrectly from executing the "Cancel" else command.
                    print()
                    print("Invalid responce, please try again")
                    action = str.capitalize(input("Action: Shop, Cancel, Checkout? "))

          if action == "Shop":
                    display_products(products, prices)

          while  action == "Shop":
                    '''(Str input) -> Str
                    while function that runs through if statements  for shop and checkout, and a
                    else statement for cancel.'''
                    print()
                    item_select = (int(input("Product number: ")) - 1)
                    cartQty[item_select]  += 1
                    print ("You added ", products[item_select], "to your cart for", "$", prices[item_select])
                    total_owed = float(total_owed) + float(prices[item_select])
                    display_cart(cartQty, products, prices)
                    print()
                    action = str.capitalize(input("Action: Shop, Cancel, Checkout? "))
                    
          if action == "Checkout":
                    '''(Str input) -> none
                    Displays shopping cart'''
                    display_cart(cartQty, products, prices)
                    print()
                    print ("Checking out, please pay for the contents of your shopping cart")
                    print()
                    print("Please pay ","$" + format(total_owed, ".2f")) # EXTRA CREDIT 2
                    print()
                    print("Thank you for shopping at ShopMart")
                    end_program = "end"

          if action == "Cancel":
                    print()
                    print("Thanks for visiting Shopmart")
                    total_owed = 0.0
                    print()
                    print("You cancelled your order, so you owe us nothing.")
                    end_program = "end"
          
print()
print("ShopMart thanks you for shopping with us")


          




          
