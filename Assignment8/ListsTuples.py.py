
def read_customers_from_file(filename):
    customers = []
    
#     #load file parameter fileName type string
    try:
       with open(filename, 'r', newline='', encoding='utf-8') as file:
        for line in file:
              # Strip whitespace and newline characters
            line = line.strip()

            # Split the Line into Fields by comma
            customer_data = line.split('","')
            # Remove leading and trailing quotes from each field
            customer_data = [field.strip('"') 
                              for field in customer_data
                            ]
            # Append the tuple to the customers list
            customers.append(tuple(customer_data))

        return customers
    except FileNotFoundError:
       print(f"Error: File '{filename}' Not found.")
       return []
    except Exception as e:
       print(f"An error occurred while reading the file: {e}")
       # Returns a new list of customers sorted by the field at key_index
def sort_customers(customers, key_index):
    # Python's built-in sorted function sorted()
    # customers []
    # Sort the list based on the value at the given index
    # key is a variable name
    # lambda is used to define anonymous (unnamed) functions in one line
    sorted_list = sorted(customers, key=lambda customer: customer[key_index])
    return sorted_list

#  Displays selected fields from each customer.
# Parameters:
        # customers : list of tuple
        # fields_to_show : list of tuple (str, int)

def display_customers(customers, fields_to_show):
    for customer in customers:
        output = ' '

        for label, index in fields_to_show:
            value = customer[index]
            output += label + ':  ' + value + ', '
            output = output.rstrip(', ')
        print(output)

#"Returns a list of customers contains search_term.
def search_customers(customers, search_term, key_index):
    matching_customers = [] # Start with an empty list

     # Convert the search term to lowercase to make the search case-insensitive
    search_term = search_term.lower()

     # for each customer
    for customer in customers:
        field_value = customer[key_index].lower() # the field search 

        # if the search term is found in the field value
        if search_term in field_value:
            matching_customers.append(customer) # add to the result list

    # Return the list of matches
    return matching_customers

# Handles user input for searching by company or contact name.
def handle_search(customers):
    print("\n--- Search Menu ---")
    print("1. Search by Company Name")
    print("2. Search by Contact Name")
    choice = input("Enter choice (1 or 2): ").strip()
    search_term = input("Enter search term (full or partial name): ").strip()

    if choice == "1":
        key_index = 1 # Company Name
        fields = [('Company', 1), ('Contact', 2), ('Phone', 9)]
        results = search_customers(customers, search_term, key_index)
        print(f"\nResults for Company Name containing '{search_term}':")
    elif choice == "2":
        key_index = 2  # Contact Name
        fields = [('Contact', 2), ('Company', 1), ('Phone', 9)]
        results = search_customers(customers, search_term, key_index)
        print(f"\nResults for Contact Name containing '{search_term}': ")
    else:
        print("Invalid choice.")
        return
    
    if results:
        display_customers(results, fields_to_show=fields)
    else:
        print("No matching records found.")

def main():
    filename = 'CustomerList.txt'
    customers = read_customers_from_file(filename)

    # 1. Display company name, contact name, and phone number
    print("Sorted by Company Name:")
    sorted_by_company = sort_customers(customers, key_index=1)
    display_customers(sorted_by_company, 
                      fields_to_show=[('Company', 1), 
                                      ('Contact', 2), 
                                      ('Phone', 9)
                                      ]
                      )
    
    # 2. Display all customers sorted by Contact Name
    print("Sorted by Contact Name:")
    sorted_by_contact = sort_customers(customers, key_index=2)
    display_customers(sorted_by_contact, 
                      fields_to_show=[('Contact', 2),
                                      ('Company', 1), 
                                      ('Phone', 9)
                                     ]
                      )
    
    # Handle search by company or contact name
    handle_search(customers)

# Run the program
if __name__ == '__main__':
   main()