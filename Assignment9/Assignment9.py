import csv

def read_customers_from_file(filename): 
    customers = []

    try:
        with open(filename, 'r', newline='', encoding='utf-8') as file:
            #csv.DictReader to read each row as a dictionary
            reader = csv.DictReader(file)
            for row in reader:
                customers.append(row)
            # Append each row dictionary to the customers list
            return customers

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return []
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return []
    
def customers_by_company_sorted(customers):
      #Display customers sorted by company name
    customers_sorted = sorted(customers, key=lambda com: com['CompanyName'])    
  # Display company name, contact name, and phone number
    print("Sorted by Company Name:")
    print("-" * 80)
    print(f"{'Company Name':<35} {'Contact Name':<25} {'Phone Number':<15}")
    print("-" * 80)
    for cus in customers_sorted:
        print(f"{cus['CompanyName']:<35} | {cus['ContactName']:<25} | {cus['Phone']:<15}")
    print("\n")

def customers_by_contact_sorted(customers):
    customers_sorted = sorted(customers, key=lambda con: con['ContactName'])  
    print("Sorted by Contact Name:")
    print("-" * 80)
    print(f"{'Contact Name':<25} {'Company Name':<35} {'Phone Number':<15}")
    print("-" * 80)
    for cus in customers_sorted:
        print(f"{cus['ContactName']:<25} |{cus['CompanyName']:<35} | {cus['Phone']:<15}")
    print("\n")

def search_company(customers):
    # Search for a company name
    search_term = input("Enter company name or part of a name to search: ").strip().lower()

    print("\nSearch Results:")
    print("-" * 85)

    matches = [c for c in customers if search_term in c['CompanyName'].lower()]

    if matches:
        for c in matches:
            print(f"Customer ID  : {c.get('CustomerID', '')}")
            print(f"Company Name : {c.get('CompanyName', '')}")
            print(f"Contact Name : {c.get('ContactName', '')}")
            print(f"Contact Title: {c.get('ContactTitle', '')}")
            print(f"Address      : {c.get('Address', '')}")
            print(f"City         : {c.get('City', '')}")
            print(f"Country      : {c.get('Country', '')}")
            print(f"Phone        : {c.get('Phone', '')}")
            print(f"Fax          : {c.get('Fax', '')}")
            print("-" * 85)
    else:
        print("No matching companies found.\n")

def search_contact(customers):
    #Search for a contact name 
    search_term = input("Enter contact name or part of a name to search: ").strip().lower()

    print("\nSearch Results:")
    print("-" * 85)

    # Find all records where the contact name contains the search term (case-insensitive)
    matches = [c for c in customers if search_term in c['ContactName'].lower()]

    if matches:
        for c in matches:
            print(f"Customer ID  : {c.get('CustomerID', '')}")
            print(f"Company Name : {c.get('CompanyName', '')}")
            print(f"Contact Name : {c.get('ContactName', '')}")
            print(f"Contact Title: {c.get('ContactTitle', '')}")
            print(f"Address      : {c.get('Address', '')}")
            print(f"City         : {c.get('City', '')}")
            print(f"Country      : {c.get('Country', '')}")
            print(f"Phone        : {c.get('Phone', '')}")
            print(f"Fax          : {c.get('Fax', '')}")
            print("-" * 85)
    else:
        print("No matching contact names found.\n")


def main():
    filename = 'CustomerList.txt'
    customers = read_customers_from_file(filename)
   
# dictinary in curly braces {} colon : to separate key and value
 # Sort customers by company name
    customers_by_company_sorted(customers)
# Sort customers by contact name
    customers_by_contact_sorted(customers)
    # search function
    while True:
        print("\n--- Search Menu ---")
        print("1. Search by Company Name")
        print("2. Search by Contact Name")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ").strip()

        if choice == '1':
            search_company(customers)
        elif choice == '2':
            search_contact(customers)
        elif choice == '3':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
    
# Run the program
if __name__ =='__main__':
    main()

    