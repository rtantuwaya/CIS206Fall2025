import re
# Imports Python’s built-in regular expression module.

def remove_multiple_spaces(text):
    # Pattern: one or more spaces  replace with a single space
    return re.sub(r'\s+', ' ', text)
    # r'\s+'
    # \s - matches any whitespace charcter
    # +  - means one or more occurrences
    # \s+ - matches every sequence of one or more spaces
# Test string
text = 'Python      Exercises'
result = remove_multiple_spaces(text)

print("Original text:", repr(text))
print("Modified text:", repr(result))
