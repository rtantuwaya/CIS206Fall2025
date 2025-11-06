import re
# Imports the regular expression module

def replace_with_colon(text):
    # Pattern: match space, comma, or dot
    pattern = re.compile(r'[ ,.]')
    # r'[ ,.]' 
    # [...] defines a character class, it matches any one of the listed characters
    # space ' '
    # comma ','
    # dot '.'

    # Replace them with colon (:)
    return pattern.sub(':', text)
 # pattern.sub(':', text)
 # .sub() - replaces all matches of the pattern with the string ':'

# Test string
text = 'Python Exercises, PHP exercises.'
result = replace_with_colon(text)

print("Original text:", text)
print("Modified text:", result)
