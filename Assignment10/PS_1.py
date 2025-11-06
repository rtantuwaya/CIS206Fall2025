import re
# Imports Python's re module
# The re module lets us check patterns inside text

def is_allowed_string(s):
# Defines a function called is_allowed_string that take one arguments s the string to test
    pattern = re.compile(r'^[a-zA-Z0-9]+$')
# This line creates aregular expression pattern and compiles it for resue
    # ^ Start string
    # only allows a–z, A–Z, and 0–9
    # + One or more
    # $ End of the string
    return bool(pattern.match(s))
# if it matches, it returns a match object.
# Wrapping it with bool() converts that do
# True - if mathch found
    # False - if no match

test_string = ["ABCDEFabcdef123450", "*&%@#!}{"]

for text in test_string:
    # Loop through each string (text) in the list
    #  # Calls the function is_allowed_string
    if is_allowed_string(text):
        print(f"'{text}' is valid (contains only a-z, A-Z, 0-9).")
    else:
        print(f"'{text}'is NOT valid (contains other characters).")