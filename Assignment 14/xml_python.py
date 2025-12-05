# Step 1: Import the SAX library
import xml.sax
# SAX = Simple API for XML
# SAX reads XML one piece at a time, instead of loading the whole file.
  
# Step 2: Create a handler class
class LibraryHandler(xml.sax.ContentHandler):
    # A handler tells SAX what to do when it finds:
        #1 <tag> startElement 
        #2 text characters 
        #3 </tag> endElement
    # SAX calls these automatically while reading the XML file.

# Step 3 Set up variables in init()

    def __init__(self):
        super().__init__()
        self.current = ""          # Tracks which tag we are inside
        self.temp_title = ""       # Temporary storage for <title>
        self.temp_author = ""      # Temporary storage for <author>
        self.temp_year = ""        # Temporary storage for <year>
        self.temp_available = ""   # Temporary storage for <available>
    # These variables store the text inside the XML tags, until Python finishes a tag.

# Step 4 When a tag starts (startElement)
    def startElement(self, name, attrs):
        self.current = name     

        if name == "book":
            print("\n--- Book ---")
 # This runs when SAX sees:
    # <book> 
    # <title> 
    # <author> 
    # <year> 
    # <available>
 # self.current = name remembers what tag we are inside.
 # When a new <book> starts, Python prints "Book".

 # Step 5 When text appears (characters)   
    # Called when text appears inside an element
    def characters(self, content):
        text = content.strip()
        if not text:
            return

        if self.current == "title":
            self.temp_title += text

        elif self.current == "author":
            self.temp_author += text

        elif self.current == "year":
            self.temp_year += text

        elif self.current == "available":
            self.temp_available += text
    # SAX calls this MANY TIMES for every piece of text.
        # Inside <title>To Kill a Mockingbird</title>
        # Inside <author>Harper Lee</author>
    # Python stores the text in temp variables until tag ends.

 # Step 6 When a tag ends (endElement)
     # Called when a closing tag appears
    def endElement(self, name):

        if name == "title":
            print(f"Title:     {self.temp_title}")
            self.temp_title = ""

        elif name == "author":
            print(f"Author:    {self.temp_author}")
            self.temp_author = ""

        elif name == "year":
            print(f"Year:      {self.temp_year}")
            self.temp_year = ""

        elif name == "available":
            print(f"Available: {self.temp_available}")
            self.temp_available = ""

        # Reset tag tracker
        self.current = ""


# Step 7 Create SAX parser and read the XML file

handler = LibraryHandler()          #1 Create the handler object
parser = xml.sax.make_parser()      #2 Create the XML parser
parser.setContentHandler(handler)   #3 Attach handler
parser.parse("pageviews.xml")       #4 Read pageviews.xml file line by line