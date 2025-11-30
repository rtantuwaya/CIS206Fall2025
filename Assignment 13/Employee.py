# Step 1  Define the Employee class

class Employee:
 # This create class called Employee
 # A class is like a blueprint for making .
    def __init__(self, name, idNumber, department="", position=""):
    # This is the constructor. __init__ To sets up name, ID, department, position
    # It runs automatically, afte create a employee object
        self.name = name
        # Stors the employee's name inside the object
        self.idNumber = idNumber
        # Store the employee's ID number inside the object
        self.department = department
        # Store the deartment Default s "" (empty string) inside the object
        self.position = position
        # Store the position. Default is "" inside the object

# What python does here
#Step 1 Python reads the class definition 
    # 1. Create a blueprint in memory called Employee
    # 2. It read the method __init__(constructor)  inside the class and store
    # 3. At this point Python does not run any code __init__ yet, because we havn't created an object.

# It like Python preparing a mold(temporary structure or container mold or storage box) 
# for making Epmloyee objects, but no employees exit yet.

# Child class (inherits from Employee)
class Manager(Employee):
    # Manager is a type of Employee.
    # ingerit(name, idNumber, department, position)
    def __init__(self, name, idNumber, department, position, employees=None):
        # Call the parent (Employee) constructor
        super().__init__(name, idNumber, department, position)
        # This calls the parent constructor

        # Add new attribute for Manager
        if employees is None:
            employees = []

        self.employees = employees   # List of employees they manage

    def add_employee(self, employee):
        self.employees.append(employee)
        #step1 Python looks at self.employee
        #step2 Python runs .append(employee)

    def list_employees(self):
        print(f"{self.name} manages:")
        # Execute the first line
        for emp in self.employees:
            # Python reads the for loop
            print(" -->", emp.name)
            # First loop iteration

# Step 2 Create Employee objects

emp1 = Employee("Susan Meyers", 47899, "Accounting", "Vice President")
# Create Emplpyee object for data Susan
emp2 = Employee("Mark Jones", 39119, "IT", "Programmer")
# Create Employee object for data Mark
emp3 = Employee("Joy Rogers", 81774, "Manufacturing", "Engineer")
# Create Employee object for Joy

# Step 2: Python reads object creation

# emp1 = Employee("Susan Meyers", 47899, "Accounting", "Vice President")

# What happens here
    # 1 Python sees Employee(. . . .) it knows we want to create a new object using the Employee class.
    # 2 Python allocates memory for this new object.
    # 3 Python calls the __init__ constructor automatically with the arguments. 
        # * name - "Susan Meyers"
        # * idNumber - 47899
        # * department - "Accounting"
        # * department - "Vice President"
    # 4 inside __init__, Python executes the lines

#  self.name = name 
#  self.idNumber = idNumber
#  self.department = department
#  self.position = position

  # * self refers to the new object being created (emp1)
  # * These lines store the data inside the object.

  # 5 After the constructor finishes, Python retruns the new Employee object and 
  # assigns to the varaible emp1. 
# Now we have an Employee object in memeory with all its data sored

# Step 3: Repeat object creation for emp2 and emp3
# emp2 = Employee("Mark Jones", 39119, "IT", "Programmer")
# emp3 = Employee("Joy Rogers", 81774, "Manufacturing", "Engineer")

# Create a Manager (child class)
mgr = Manager("Alice Brown", 22222, "Management", "Department Manager")

#step 4 Creating a Manager object
  #1 Sees Manager( ) wants to create a Manager
  #2 Allocates memory for the new Manager object (mgr)
  #3 Calls the Manager constructor:
  # Manager.__init__(mgr, "Alice Brown", 22222, "Management", "Department Manager", employees=None)

  # 4 Inside Manager init
  # call - super().__init__(name, idNumber, department, position)
  # Employee.__init__(mgr, "Alice Brown", 22222, "Management", "Department Manager")

  #5 Employee constructor runs
    # self.name = "Alice Brown"
    # self.idNumber = 22222
    # self.department = "Management"
    # self.position = "Department Manager"

  #6 Back to Manager constructor
  #     if employees is None:
  #   employees = []
   # self.employees = employees


# Print details of each employee
print("Name:", emp1.name)
# emp1.name Access the name of the first Employee
print("ID Number:", emp1.idNumber)
# emp1.idNumber Access the ID number of the first Employee
print("Department:", emp1.department)
# emp1.department Access the deartment
print("Position:", emp1.position)
# emp1.position Access the position
print("-------------------------")

print("Name:", emp2.name)
# emp2.name Access the name of the first Employee
print("ID Number:", emp2.idNumber)
# emp2.idNumber Access the ID number of the first Employee
print("Department:", emp2.department)
# emp2.department Access the deartment
print("Position:", emp2.position)
# emp2.position Access the position
print("-------------------------")

print("Name:", emp3.name)
# emp3.name Access the name of the first Employee
print("ID Number:", emp3.idNumber)
# emp3.idNumber Access the ID number of the first Employee
print("Department:", emp3.department)
# emp3.department Access the deartment
print("Position:", emp3.position)
# emp3.position Access the position
print("-------------------------")

# Add employees to the manager
mgr.add_employee(emp1)
#when this method is called
#1 mgr is the Manager object
#2 Python passes mgr as self 

 #It become internally add_employee(mgr, emp1)

mgr.add_employee(emp2)
#It become internally add_employee(mgr, emp2)

# Show the list of managed employees
mgr.list_employees()
# Calling the method
# Python pass mgr as self

# Show the list of managed employees
# Step 4: Python reads print statements

# What happen here 
    # 1. Python see emp1.name it goes to the emp1 object in memory and read the value "Susan Meyers"
    # 2. It does the same for emp1.idNumber, emp1.department, and emp1.position.

# Summary of Python's flow
    # 1. Read the class definition  store it as a blueprint
    # 2. Create objects call __init__ constructor  store data inside each object
    # 3. Access object varables  use print() to show data