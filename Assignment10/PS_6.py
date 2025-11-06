import re
# import re, This imports Python's Regular Expression(regex) module

def match_word_with_z(s):
# This defines a function named match_word_with_z that takes 
# one arguments s the string to be checked
    pattern = re.compile(r'\b\w*z\w*\b', re.IGNORECASE)
    # re.compiler() prepares (compiles) a regular expression pattern
    # \b - Word boundary (ensures we match whole words)
    # \w* - Zero or more word characters (letters, digits, underscores)
    # z - The word must contain the letter ‘z’
    # \w* -  Zero or more word characters (letters, digits, underscores)
    # \b - Word boundary (ensures we match whole words)
    # re.IGNORECASE - Makes it match both lowercase and uppercase ‘z’.
    return pattern.findall(s)
    # pattern.findall - Finds all matching words in the given string s
    # Returns a list of matches.


test_string = ["The quick brown fox jumps over the lazy dog.",
               "Python Exercises."
              ]
# This creates a list of the test strings to check one by one

for text in test_string:
    # Loop through each string (text) in the list
    result = match_word_with_z(text)
       # Calls the function match_word_with_z() for the current string
    if result:
 
     # If it retrun True, it matches the pattern
        print(f"'{text}' Words containing 'z': '{result}'")
    else:
        print(f"'{text}' No words contain 'z'")