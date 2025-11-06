import re
# Imports the regular expression library

def extract_date_from_url(url):
    # Pattern: match /YYYY/MM/DD/ inside the URL
    pattern = re.compile(r'/(\d{4})/(\d{2})/(\d{2})/')
 # / - ensures we look for slashes around the date parts
 # (\d{4}) - captures 4 digits (the year)
 # / - ensures we look for slashes around the date parts
 # (\d{2}) - captures 2 digits (month)
 # / - ensures we look for slashes around the date parts
 # (\d{2}) - captures 2 digits (day)

    match = pattern.search(url)
 # pattern.search(url) - Looks for the first match of this pattern inside the URL 
 # .search(url) finds a match, it returns a match object.  
    if match:
        year, month, day = match.groups()
# match.groups() - Returns a tuple of the three captured parts: (year, month, day)
# .groups() extracts all captured groups and returns them as a tuple:
        print(f"URL: {url}")
        print(f"Year : {year}")
        print(f"Month: {month}")
        print(f"Day  : {day}")
    else:
        print("No date found in the URL.")

# Test URL
url = "https://www.washingtonpost.com/news/football-insider/wp/2016/09/02/odell-beckhams-fame-rests-on-one-stupid-little-ball-josh-norman-tells-author/"
extract_date_from_url(url)
