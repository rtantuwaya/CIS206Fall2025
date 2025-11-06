import re
# Imports the regular expression module for pattern-based replacements.

def replace_whitespace_and_underscore(text):
    if " " in text:
# if " " in text:- Checks if there are spaces in the text.
        return re.sub(r'\s', '_', text)
 # replaces all spaces (\s) with underscores (_)
 
    elif "_" in text:
# elif "_" in text: If there are underscores - replaces them with spaces.
        return re.sub(r'_', ' ', text)
# re.sub(pattern, replacement, text) - 
# Replaces all matches of the pattern with the given replacement.
    else:
        return text  # If neither, return unchanged

# Test cases
test_strings = ["Regular Expressions", "Code_Examples"]

for text in test_strings:
    result = replace_whitespace_and_underscore(text)
    print(f"Original: '{text}'  Modified: '{result}'")
# The loop runs through both test strings and prints the before-and-after results