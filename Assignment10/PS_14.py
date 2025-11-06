import re
# Imports the regular expression module.

def find_words_starting_with_a_or_e(text):
    # Pattern: words starting with 'a' or 'e' - '\b[aeAE]\w*'
    pattern = re.compile(r'\b[aeAE]\w*')
    # \b - Word boundary
    # [aeAE] - Matches any word that starts with ‘a’ or ‘e’ (case-insensitive)
    # \w* - Matches the rest of the word (letters, numbers, or underscore)
    return pattern.findall(text)
   # .findall(text) - Finds all occurrences of words
   # pattern - match the pattern
   # returns - Returns a list of words

# Test string
text = ("The following example creates an ArrayList with a capacity of 50 elements. "
        "Four elements are then added to the ArrayList and the ArrayList is trimmed accordingly.")

result = find_words_starting_with_a_or_e(text)

print("Words starting with 'a' or 'e':")
print(result)
