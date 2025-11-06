import re
# Imports Python’s regular expressions module.

def search_words(text, words):
    for word in words:
    # Loops through the list of words
        if re.search(r'\b' + re.escape(word) + r'\b', text):
        # re.escape(word)
        # Escapes any special regex characters inside the word
        # r'\b' - Word boundary
        # re.escape(word) - characters inside the word
        #  r'\b' - Word boundary
        # re.search(pattern, text)
        # Searches the entire string for the pattern.
            print(f"'{word}' Found in text")
        else:
            print(f"'{word}' Not found in text")

# Sample text and searched words
sample_text = 'The quick brown fox jumps over the lazy dog.'
searched_words = ['fox', 'dog', 'horse']

search_words(sample_text, searched_words)
# Searches the entire string for the pattern.


 