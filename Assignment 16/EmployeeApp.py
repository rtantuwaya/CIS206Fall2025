#1 Python reads the import statements
import json
#json is used for saving and loading employee data.
import tkinter as tk
# tkinter is used to create the GUI window
from tkinter import messagebox
# messagebox is used for pop-up alerts


#2 Python reads the Employee class definition
class Employee:
    def __init__(self, name, idNumber, department="", position=""):
        self.name = name
        self.idNumber = idNumber
        self.department = department
        self.position = position
# It only creates the class blueprint so the program can later create Employee objects.


#3 Python reads the EmployeeManager class definition
 # This class handles JSON saving/loading and manages all employees.

class EmployeeManager:
    # Python reads and stores the __init__ methods
    def __init__(self, filename="employees.json"):
        self.filename = filename
        # Sets the filename the manager  will use
        self.employees = []
        # Creates an empty list for employee
        self.load_json()
        # Calls load_json() automatically goto step 8

    # reads and stores the add_employee methods
    def add_employee(self, employee):
        self.employees.append(employee)
        self.save_json()

    # reads and stores the delete_employee methods
    def delete_employee(self, index):
        if 0 <= index < len(self.employees):
            del self.employees[index]
            self.save_json()

    # reads and stores the save_json methods
    def save_json(self):
        data = []
        for emp in self.employees:
            data.append({
                "name": emp.name,
                "idNumber": emp.idNumber,
                "department": emp.department,
                "position": emp.position
            })

        with open(self.filename, "w") as file:
            json.dump(data, file, indent=4)

 # step 8 Python runs load_json()
     # reads and stores the load_json methods
    def load_json(self):
        try:
            # If employees.json exists 
            with open(self.filename, "r") as file:
                data = json.load(file)
                # loads all employees
                for item in data:
                    emp = Employee(
                        item["name"],
                        item["idNumber"],
                        item["department"],
                        item["position"]
                    )
                    self.employees.append(emp)
 # If it does not exist 
        except FileNotFoundError:
            self.employees = []
    # creates an empty list and continues with no errors
# this above method load_json() does Previously saved employees or create An empty list if none exist 

# 4 Python reads the EmployeeApp class definition
# GUI Application (Tkinter)
# This class creates the entire GUI.
# Step 10 inside EmployeeApp init method
class EmployeeApp:
    def __init__(self, manager):
        # The GUI window is created and prepared.
     #1 self.manager stores the EmployeeManager object
        self.manager = manager
     
      #2 A Tkinter window opens:
        self.root = tk.Tk()
        self.root.title("Employee Manager")
        self.root.geometry("350x500")

    #3 Python creates labels, entry fields, and buttons
        # ------- Input Fields -------
        tk.Label(self.root, text="Name").pack()
        self.name_entry = tk.Entry(self.root, width=30)
        self.name_entry.pack()

        tk.Label(self.root, text="ID Number").pack()
        self.id_entry = tk.Entry(self.root, width=30)
        self.id_entry.pack()

        tk.Label(self.root, text="Department").pack()
        self.dep_entry = tk.Entry(self.root, width=30)
        self.dep_entry.pack()

        tk.Label(self.root, text="Position").pack()
        self.pos_entry = tk.Entry(self.root, width=30)
        self.pos_entry.pack()

        #  ------- Buttons -------
        #4 Buttons are linked to functions: Add Employee  self.add_employee_gui
        tk.Button(self.root, text="Add Employee",
                  command=self.add_employee_gui).pack(pady=10)

        #5 Buttons are linked to functions: Delete  self.delete_employee_gui
        tk.Button(self.root, text="Delete Selected Employee",
                  command=self.delete_employee_gui,
                  fg="white", bg="red").pack(pady=5)

        # ------- Listbox ------ Python creates a listbox to display employees 
        self.listbox = tk.Listbox(self.root, width=50, height=15)
        self.listbox.pack()

        # Load saved employees
        self.refresh_listbox()
        # call refresh_listbox() method 
        # to show all employees loaded from JSON


    # Add employee to list
    # Python loads add_employee_gui methods
    def add_employee_gui(self):
        name = self.name_entry.get()
        id_num = self.id_entry.get()
        dep = self.dep_entry.get()
        pos = self.pos_entry.get()

        if name == "" or id_num == "":
            messagebox.showerror("Error", "Name and ID are required!")
            return

        emp = Employee(name, id_num, dep, pos)
        self.manager.add_employee(emp)
        self.refresh_listbox()

        self.name_entry.delete(0, tk.END)
        self.id_entry.delete(0, tk.END)
        self.dep_entry.delete(0, tk.END)
        self.pos_entry.delete(0, tk.END)

    # Delete selected employee
    # Python loads delete_employee_gui methods
    def delete_employee_gui(self):
        selected = self.listbox.curselection()

        if not selected:
            messagebox.showwarning("Warning", "Please select an employee to delete.")
            return

        index = selected[0]

        # Confirm delete action
        confirm = messagebox.askyesno(
            "Confirm Delete",
            "Are you sure you want to delete this employee?"
        )
        if confirm:
            self.manager.delete_employee(index)
            self.refresh_listbox()



    # Refresh list
    # Python loads refresh_listbox methods 
    def refresh_listbox(self):
        self.listbox.delete(0, tk.END)
        for emp in self.manager.employees:
            line = f"{emp.name} (ID: {emp.idNumber}) - {emp.department}, {emp.position}"
            self.listbox.insert(tk.END, line)

    # Python loads run methods 
    def run(self):
        self.root.mainloop()
    # opens the window
    # Keeps the program running
    # Wait for user action(button clicks, typing, selecting)


# All the  above classes and inside of function(method) is only defined not executed.

#5 Python reaches thr Main Program Start
# This is where the program actually starts running
# 6. Python checks: am I running this file directly?
    # Yes so the inside code runs.
if __name__ == "__main__": 
 # Step 7  Python creates an EmployeeManager object
    manager = EmployeeManager() # When this line runs
 # Step 7.1 __init__ of EmployeeManager is called from step 8 called load_json() method

 # Step 9 Python creates the GUI application
    app = EmployeeApp(manager)
 # it called EmployeeApp class which is step 4 it will call step 10
 # this runs, __init__ of EmployeeApp executes,

 # step 11 Python runs the GUI loop
    app.run()
# This calls: self.root.mainloop()
