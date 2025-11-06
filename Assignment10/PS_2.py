import re
# import re, This imports Python's Regular Expression(regex) module

def matche_string(s):
# This defines a function nameed matche_string that takes 
# one arguments s the string to be checked
    pattern = re.compile(r'ab*')
    # re.compiler() prepares (compiles) a regular expression pattern
    # Pattern: 'a' followed by zero or more 'b's
    # 'a' the string start with the letter a
    # 'b*' after a, there can be zerp or more
    return bool(pattern.fullmatch(s))
    # pattern.fullmatch(s) tries to match the string s to the pattern
    # if it matches, it returns a match object.
    # Wrapping it with bool() converts that do
    # True - if mathch found
    # False - if no match


test_string = ["ab", "abc", "a", "ab", "abb"]
# This creates a list of the test strings to check one by one

for text in test_string:
    # Loop through each string (text) in the list
    if matche_string(text):
    # Calls the function matches_string() for the current string
     # If it retrun True, it matches the pattern
        print(f"'{text}' Match found")
    else:
        print(f"'{text}' No match")