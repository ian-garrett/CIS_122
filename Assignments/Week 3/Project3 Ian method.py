# Week 3 Project "Palindrome"
# by Ian Garrett


original_string = input('Enter two-word phrase in all lowercase letters here: ')

modified_string = original_string.replace(' ', '') 
    
string_length = int(len(modified_string))
beg_point = 0

for i in range(string_length):
        if modified_string[i] == modified_string[-(i+1)]:
            beg_point = beg_point + 1
if beg_point == string_length:
    print ('Phrase is a Palindrome')
else:
    print ('Phrase is not a Palindrome')


