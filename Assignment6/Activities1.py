# Ravindra Tantuwaya
# Session 6 - Strings
#   
# Create a program that asks the user for an input string of alphabetic characters.
# Convert the string to a run-length encoded (RLE) string of characters and numbers. 


def stringProcessing(input_str):

    # Performs run-length encoding on an alphabetic string.

    # Each sequence of the same character is replaced by the character 
    # followed by the number of repetitions. 
    # Single characters remain as is.

    # Parameters:
    #    input_str: The input string to be encoded. Must contain only alphabetic characters.

    # Returns:
    #    input_str: The run-length encoded version of the input string.

    # Raises:
    #    TypeError: If input_str is not a string.
    #    ValueError: If input_str contains non-alphabetic characters.

    if not isinstance(input_str, str):
        raise TypeError("Input must be a string.")

    if not input_str.isalpha():
        raise ValueError("Input must contain alphabetic characters only.")

    encoded = ""
    i = 0
    while i < len(input_str):
        count = 1
        while i + 1 < len(input_str) and input_str[i] == input_str[i + 1]:
            count += 1
            i += 1
        encoded += input_str[i] + (str(count) if count > 1 else "")
        i += 1
    return encoded


def runLengthEncode(input_str):

    #  Validates the input and returns the run-length encoded version of the string.
    #  Returns a formatted error message instead of raising an exception.

    # Parameters:
    #    input_str : The user provided input string.

    # Returns:
    #    input_str : Encoded string if input is valid; error message otherwise.

    if not isinstance(input_str, str):
        return "Error: Input must be a string."

    if not input_str:
        return "Error: Input cannot be empty."

    if not input_str.isalpha():
        return "Error: Input must contain alphabetic characters only."

    try:
        return stringProcessing(input_str)
    except (TypeError, ValueError) as e:
        return f"Error: {e}"


def main():
    # Main function that runs the program.
    # It prompts the user for input, performs run-length encoding,
    # and prints the result or an error message.

    user_input = input("Enter a string of alphabetic characters: ")
    result = runLengthEncode(user_input)
    print("Run-Length Encoded string:", result)

# Run the program
main()
