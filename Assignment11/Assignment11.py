# Step 1- Import the required modules
import sqlite3 
#In SQ light - import SQlight3 to connect and work with SQLite database
# sqlignt is a built-in Python library
# it allows our program open .db files, send SQL commands, and results.
from prettytable import PrettyTable  # makes table output neat
# prettyTable is an external module, it makes the output look an actual database table

# Step 1. Define a function 
def get_table_names(cursor):
    # This function receives cursor, Which is used to run SQL commands.
    # It will return a list of all table names in the SQLite database
# Step 2 - run SQL query to get tables
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;")
# cursor.execute - execute sql query
# sqlite_master is a special system table that exists inside every SQLite database
# sqlite_master is a metadata table that tells SQLite 
# what objects(tables, indexes, triggers, views)exit in the database 
# used
# SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;
# Give me all items where type = table 

# Step 3  -Fetch all result 
    tables = [] 
    rows = cursor.fetchall()
    # cursor.fetchall() Give me all the rows that were returned by the last SQL query.
    # get all rows from database
    for row in rows:
    # loop through each row
        tables.append(row[0])
        # take the first column(table name)
        # add it to the list
    return tables

# Step 3. Define a function to display a selected table
def display_table(cursor, table_name):
    #Display all records from the selected table.
    cursor.execute(f"SELECT * FROM {table_name};")
    # rows holds all the records from table
    rows = cursor.fetchall()
    # cursor.description gives column details  - Extract the column names
    col_names = [desc[0] for desc in cursor.description]

    # Using PrettyTable for clean output formatting
    # create new PrettyTable object
    table = PrettyTable()
    # The first column will be "Row#" to show row numbers.
    table.field_names = ["Row#"] + col_names
    
    for idx, row in enumerate(rows, start=1):
        table.add_row([idx] + list(row))
    
    print(f"\n=== Contents of table: {table_name} ===")
    print(table)
    return col_names, rows

# insert record
# step 1 = Function definition 
def insert_record(cursor, conn, table_name, col_names): 
 #Insert a new record into the table
 # Parameters:
 #      cursor: SQLite cursor object
 #        conn: SQLite connection object
 #      table_name (str): Name of the table
 #      col_names (list): Listof column names
 # This defines a function 
 #  cursor - executes SQL commands
 #  conn - commits changes to the database
 # table_name - name of the table
 # col_name - list of column names in that table
 # 

 # step 2- Tell the user what to do
    print("\nEnter values for each field (press Enter to skip optional fields):")

# step 3 - For each column, ask the user for a value
    values = []
    for col in col_names: # Goes through each column name
        val = input(f"{col}: ").strip()  # Ask the user to type a value for that column
        # .strip() removes accidental spaces user mau input

# Step 4 - Convert blank input to None
        if val == "": # If the user process Enter Without typing anything 
            values.append(None) #  store None (NULL in SQL)
        else:
            values.append(val) # store the value normally

# Step 5 - Create SQL placeholders for value binding
    placeholders = ",".join(["?"] * len(values)) 
    # these placehoder prevent SQL injection(wrong input data) and allows safe insertion.

# Step 6 - Build the SQL INSERT statement
    query = f"INSERT INTO {table_name} ({','.join(col_names)}) VALUES ({placeholders});"
    # ','.join(col_names) it is not comma after table it's between column bames, inside if parentheses , 

# Step 7 - Try to insert the record
    try:
        cursor.execute(query, values) # cursor.execute send the SQL commad 
        conn.commit() # saves the change.
        print("Record inserted successfully!")

# Step 8 - if something goes wrong, show error
    except sqlite3.Error as e:
         print("Error inserting record:", e)

# Update Record
# Step 1 - Function definition
def update_record(cursor, conn, table_name, col_names, rows):
    #Update a specific field in a record.
    # The function needs
    # cursor - runs SQL commands
    # conn - commits changes
    # table_name - name of the table
    # col_names - list of columns in that table
    # rows - all records already fetched from the table
    try:
 # Step 2- Ask users which row wants to update
        row_num = int(input("\nEnter Row# of record to update: ")) - 1
        # subtract 1 because Python lists start at index 0.

  # Step 3 - Validation row number
        if row_num < 0 or row_num >= len(rows):
        # if the row number exists
            print("Invalid row number.")
            return

 # Step 4 - Get the selected record
        record = rows[row_num]
        print(f"\nSelected Record: {record}")
        # Show the record are about to update

 # Step 5 - Show all fields (columns) to choose from
        for i, col in enumerate(col_names, start=1):
            print(f"{i}. {col}")

 # Step 6 - Which field (column) to update 
        field_choice = int(input("Enter number of field to update: ")) - 1
        # Validate 
        if field_choice < 0 or field_choice >= len(col_names):
            print("Invalid field choice.")
            return

# Step 7 - Get the new value from the user
        new_value = input(f"Enter new value for {col_names[field_choice]}: ")

# Step 8 - Identify the primary key
        pk_col = col_names[0]
        # The first column in the table is the primary key (pk_col = 'id')
        pk_value = record[0]
        # The first value in the row is the primary key value (pk_value = 1)

# Step 9 - Build SQL UPDATE statement
        query = f"UPDATE {table_name} SET {col_names[field_choice]} = ? WHERE {pk_col} = ?;"

# Step 10 - Execute the update 
        cursor.execute(query, (new_value, pk_value))
        conn.commit()
        print("Record updated successfully!")

# Step 11 - Handle errors
    except (ValueError, sqlite3.Error) as e:
        print("Error updating record:", e)
       
# Delete record
def delete_record(cursor, conn, table_name, col_names, rows):
    #Delete a record from the table.
    # The function needs
    # cursor - runs SQL commands
    # conn - saves (commits) changes
    # table_name - table to delete from
    # col_names - list of columns names (first coulun assumed to be primary key)
    # rows - all records currently displayed 

    try:
# Step 1 - user input 
        row_num = int(input("\nEnter Row# of record to delete: ")) - 1
        # subtract 1 because Pyhton uses 0 based indexing 

# Step 2 - Validate the row number
        if row_num < 0 or row_num >= len(rows):
            print("Invalid row number.")
            return

# Step 3 - Select the recors to delete
        record = rows[row_num]

# Step 4 - Identify the primary key
        pk_col = col_names[0]
        # The first column (col_names[0] is the PRIMARY KEY)
        pk_value = record[0]
        # The first field in the (recors[0] is the PK value)

# Step 5 - Ask the user to confirm deletion
        confirm = input(f"Are you sure you want to delete record {pk_value}? (y/n): ").lower()

# Step 6 - If user says YES, delete the record
        if confirm == "y":
            query = f"DELETE FROM {table_name} WHERE {pk_col} = ?;"
            cursor.execute(query, (pk_value,))
            conn.commit()
            print("Record deleted successfully!")
        else:
            print("Delete canceled.")
# Step 7 - Handle errors
    except (ValueError, sqlite3.Error) as e:
        print("Error deleting record:", e)


# Display table
def process_table(cursor, conn, table_name):
    # This function receives
        # cursor - executes SQL commands
        # conn - commits changes 
        # table_name - the names of the table the user is working with

# Step 1 - Start an infinite loop
    while True:
        # This loop continues until the user chooses Quits (Q)

# Step 2 - Display the table
        col_names, rows = display_table(cursor, table_name)
        # display_table() prints all rows and columns
        # it will return 
                # col_names - list of column names
                # rows - list of all records

 # Step 3- show the user the menu
        print("\nChoose an action:")
        print("\n(I) Insert  (U) Update  (D) Delete  (Q) Quit this table")

 # Step 4 - Get user choice
        action = input("Enter choice: ").strip().upper()
        # take user input, .strip() Remove spaces, .upper() Convert to uppercase ( user can type i or I)

 # Step 5 - Check the users's choice and run the correct function

        if action == "I":
            insert_record(cursor, conn, table_name, col_names)
        elif action == "U":
            update_record(cursor, conn, table_name, col_names, rows)
        elif action == "D":
            delete_record(cursor, conn, table_name, col_names, rows)
        elif action == "Q":
            break
        else:
            print("Invalid option. Please choose again.")

# Define main function to run
def main():
 
# Step 1 Define database path 
    db_path = "Northwind.db"  
    # to tells the program where the SQLite database file is located

# Step 2  Connect to database
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
    except sqlite3.Error as e:
        print("Error connecting to database:", e)
        return

 # Step 3: List all tables
    tables = get_table_names(cursor) # call get_table_names function
    if not tables:
        print("No tables found in the database.")
        return

 # Step 4: Show available tables to the user
    print("Available tables in the Northwind database:\n")
    for i, table in enumerate(tables, start=1):
        # table - list [ ]
        # enumerate(tables, start=1)
        # enumerate() is a built in (predefined) Python function.
        # The enumerate() function gives two values for each item:
        # the index number (i)
        # the item (table)
        # Puthon default 0
        # start = 1
        print(f"{i}. {table}")
    # prints all table names with a number next to each

 # Step 5: User selects a table
    try:
        choice = int(input("\nEnter the number of the table to view: "))
        # User types the number of the table
        if choice < 1 or choice > len(tables):
            print("Invalid selection.")
            return
        selected_table = tables[choice - 1]
        # Subtract 1 to convert from 1 based numbering to Python 0 based index
    except ValueError:
        print("Please enter a valid number.")
        return

 # Step 6  Display and process the selected table 
    # display_table(cursor, selected_table)
    process_table(cursor, conn, selected_table)

 # Step 7 - Close the connection
    conn.close()

if __name__ == "__main__":
   main()
