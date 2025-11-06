import re
# Imports Python’s regular expressions library.

def search_literal_with_position(text, word):
    pattern = re.compile(re.escape(word))
    # re.escape(word) - Escapes any special regex characters in word
    
    match = pattern.search(text)
# pattern.search(text) - Searches for the first occurrence of the pattern inside the text
    if match:
        print(f"'{word}' found in text!")
        print(f"Start position: {match.start()}")
    # start() gives the starting index of the match.
        print(f"End position: {match.end()}")
   # end() gives the ending index
    else:
        print(f"'{word}' not found in text.")

# Sample text and word to search
sample_text = 'The quick brown fox jumps over the lazy dog.'
searched_word = 'fox'

search_literal_with_position(sample_text, searched_word)
