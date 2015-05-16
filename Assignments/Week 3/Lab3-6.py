# Ian Garrett
# Lab 3-6

# In order to detect a palindrome, we will write a function that will:
# 1) Prompt user for a two-word phrase (using input()) and convert to lowercase
# 2) Clean the input string so it is all letters using a for loop
# 3) Create a string that reverses and returns the
#    letters of the cleaned input string
# 4) Write a def function that compares the two strings and prints a response
#    based on if the two strings are the same

# Stub Functions

def clean_string(lots_of_letters):
   print ("clean_string preteneds to clean up")
   return lots_of_letters

def reverse_string(string):
    print ("reversing the string")
    reverse = "civic"
    return reverse

# Define input string

original_string = input('Enter two-word phrase in all lowercase letters here: ').lower() # converts to lowercase


# Functions needed for program

def clean_string(original_string):
    clean_string = '' # start with an empty string to assemble clean string
    for letter in original_string:
        if letter in 'abcdefghijklmnopqrstuvwxyxz':
            clean_string = clean_string + letter
            # adds letter to empty string if letter falls in range a-z
    return (clean_string)

def reverse_string(clean_string):
    reverse_string = '' # start with an empty string to assemble reverse string
    for letter in clean_string:
        reverse_string = letter + reverse_string
        # adds reverse_string to the right of the number
    return (reverse_string)

def detect_palindrome(original_string):
    if clean_string == reverse_string:
        print ("You typed a palindrome - reads the same forward as backward")
    else:
        print ("You did not type a palindrome")


# Program itself

clean_string = '' # start with an empty string to assemble clean string
for letter in original_string:
    if letter in 'abcdefghijklmnopqrstuvwxyxz':
            clean_string = clean_string + letter
            # adds letter to empty string if letter falls in range a-z

reverse_string = '' # start with an empty string to assemble reverse string
for letter in clean_string:
        reverse_string = letter + reverse_string
        # adds reverse_string to the right of the letter

detect_palindrome(original_string)

