import re
# import re, This imports Python's Regular Expression(regex) module

def match_word_beginning(s):
# This defines a function named match_word_beginning that takes 
# one arguments s the string to be checked
    pattern = re.compile(r'^\w+')
    # re.compiler() prepares (compiles) a regular expression pattern
    # Pattern: match a word (letters) at the beginning of the string
    # ^ - match the start of the string
    # \w+ - Matches one or more word characters (letters, digits, or underscore) 
    # This pattern finds a word only if it begins right at the start (no spaces first)
    return pattern.match(s)
    # pattern.match. 
    # Returns a list of matches.


test_string = ["The quick brown fox jumps over the lazy dog.",
               " The quick brown fox jumps over the lazy dog."
              ]
# This creates a list of the test strings to check one by one

for text in test_string:
    # Loop through each string (text) in the list
    result = match_word_beginning(text)
       # Calls the function match_word_beginning() for the current string
    if result:
     # If it retrun True, it matches the pattern
        print(f"'{text}' Match found: '{result.group()}'")
    else:
        print(f"'{text}' No match")