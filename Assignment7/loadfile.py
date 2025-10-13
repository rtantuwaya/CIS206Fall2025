# Assignment 7 - File Processing Assignment
# Then repeatedly prompt the user for a name. Search the loaded file. 
# If the name is found in the file then display a message. 
# If the name is not in the file, write it to an output file (nofound.txt) 
# and display an appropriate message. 

def loadNamesFromFile(fileName: str):
#     #load file parameter fileName type string
    try:
      with open(fileName, 'r') as f:
        return [line.strip().lower() for line in f if line.strip()]
    except FileNotFoundError:
       print(f"Error: File '{fileName}' Not found.")
       return []
    except Exception as e:
       print(f"An error occurred while reading the file: {e}")

          
def appendNameToFile(fileName: str, name: str):
   
   try:
      with open('names.txt', 'a') as f:
         f.write(name + '\n')
   except Exception as e:
       print(f"Could not write to file '{fileName}': {e}")

              
def main():   
    nameFile = 'names.txt'
    notFoundfile = 'output.txt'
    knowNames = loadNamesFromFile(nameFile)
    #print(knowNames, end='')
  
    while True:
       userInput = input("Enter a string (or type 'exit' to quit): ").strip()

       if userInput.lower() == 'exit':
          print("Exiting program")
          break
       
       if not userInput:
          print("Please enter a valid name.")
          continue
       
       nameLower = userInput.lower()
       
       if nameLower in knowNames:
          print(f" The string '{userInput}' is already in the file.")
       else:
          print(f"The string '{userInput}' has been written to '{notFoundfile}.'")
          appendNameToFile(notFoundfile, userInput)
main()



