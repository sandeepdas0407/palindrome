import re

def is_palindrome(s):
      
    # Remove all non-alphanumeric characters from the string and convert it to lowercase
    s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    return s == s[::-1]



