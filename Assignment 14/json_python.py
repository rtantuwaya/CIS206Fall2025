# Step 1: Import the JSON library
import json
# Python loads the json module so it can read JSON files.


# Step 2: Open and read the JSON file
with open("pageviews.json", "r") as file:
    # Python opens the file in read mode ("r")

    data = json.load(file)
    # Python reads the entire file at once.
    # JSON text is converted into Python dictionaries and lists.


# Step 3: Get the list of books
books = data["books"]


# Step 4: Loop through each book and print the information
print("\n==============================")
print("         Library Books")
print("==============================")

for book in books:
    print("\n--- Book ---")
    print(f"Title:      {book['title']}")
    print(f"Author:     {book['author']}")
    print(f"Year:       {book['year']}")
    print(f"Available:  {book['available']}")
