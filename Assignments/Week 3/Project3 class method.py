def is_palindrome(word):
    return word == ''.join(reversed(word))
print (is_palindrome('hello'))
