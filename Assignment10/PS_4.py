import re
# import re, This imports Python's Regular Expression(regex) module

def find_lowercase_underscore(s):
# This defines a function named ind_lowercase_underscore that takes 
# one arguments s the string to be checked
    pattern = re.compile(r'[a-z]+_[a-z]+')
    # re.compiler() prepares (compiles) a regular expression pattern
    # [a-z]+  one or more lowercase letters
    # _ underscore character 
    # [a-z]+  one or more lowercase letters
    return pattern.findall(s)
    # pattern.findall Finds all non-overlapping matches in the string.
    # Returns a list of matches.


test_string = ["aab_cbbbc", "aab_Abbbc", "Aaab_abbbc"]
# This creates a list of the test strings to check one by one

for text in test_string:
    # Loop through each string (text) in the list
    result = find_lowercase_underscore(text)
       # Calls the function find_lowercase_underscore() for the current string
    if result:
 
     # If it retrun True, it matches the pattern
        print(f"'{text}' Match found: {result}")
    else:
        print(f"'{text}' No match")