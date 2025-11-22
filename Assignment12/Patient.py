# Step 1 Define the Patient class
class Patient:
# A class is like a blueprint for object (patient)
    def __init__(self, first_name, middle_name, last_name,
                 address, city, state, zip_code,
                 phone_number,
                 emergency_contact_name, emergency_contact_phone):
     # __init__ this a constructor, Python will call this automatically for new Patient 
     # The arguments in __init__(first_name,) are values must provide when creating a patient (object)
        self.first_name = first_name
        # self.first_name = first_name stores the value in the object. self means " this object's copy of the variable
        self.middle_name = middle_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.phone_number = phone_number
        self.emergency_contact_name = emergency_contact_name
        self.emergency_contact_phone = emergency_contact_phone
    # The class defines the structure of a Patient object with all required data. 

# Step 2 Define the Procedure class
class Procedure:
 # create a blueprint for medical procedure (object)
    def __init__(self, procedure_name, procedure_date,
                 practitioner_name, charges):
      # __init__ constructor accepts the name of the procedure, the date, the  practitioner_name
        self.procedure_name = procedure_name
        # self.procedure_name = procedure_name stores the value in the Procedure object 
        self.procedure_date = procedure_date
        self.practitioner_name = practitioner_name
        self.charges = charges
   # Each Procedure object can hold all relevant data about a medical procedure


# Step 3 Create Patient object
patient = Patient(
    "John", "A.", "Doe",
    "123 Main Street", "Houston", "TX", "77001",
    "555-123-4567",
    "Jane Doe", "555-987-6543"
)
# 1. Patient(arguments values) calls the constructor of the Patient class.
# 2. The values in parentheses are passed to the constructor 
# 3. Python creates a new Patient object and stores it in the varable patient
# 4. All the data(first_name, to emergency_contact_phone) is now saved inside this object. 

# Step 4 Create Procedure objects
procedure1 = Procedure("Physical Exam", "02/10/2025", "Dr. Irvine", 250.00)
procedure2 = Procedure("X-Ray", "02/10/2025", "Dr. Jamison", 550.00)
procedure3 = Procedure("Blood Test", "02/11/2025", "Nurse Williams", 140.00)
# 1. Each line creates a new Procedure object using the Procedure constructor
# 2. Python assigns the data (name, date, practitioner, charge) to the object
# 3. Variables procedure1, procedure2, procedure3 now each reference a separate procedure object. 


# Step 5 Display Patient Information
print("======= PATIENT INFORMATION =======")
print("Name:", patient.first_name, patient.middle_name, patient.last_name)
print("Address:", patient.address)
print("City:", patient.city)
print("State:", patient.state)
print("ZIP:", patient.zip_code)
print("Phone:", patient.phone_number)
print("Emergency Contact:", patient.emergency_contact_name)
print("Emergency Contact Phone:", patient.emergency_contact_phone)
print()
# 1. patient.first_name accesses the first_name stored in the patient object.
# 2. Python retrives the value and print it
# 3. Repeat for all patient fields.


# Step 6 Display Procedures information
print("======= PROCEDURE 1 =======")
print("Procedure:", procedure1.procedure_name)
print("Date:", procedure1.procedure_date)
print("Practitioner:", procedure1.practitioner_name)
print("Charge: $", procedure1.charges)
print()
# 1. procedure1.procedure_name accesses the procedure name stored in the first Procedure object. 
# 2. Python prints it along with the date, practitioner and charge
 

print("======= PROCEDURE 2 =======")
print("Procedure:", procedure2.procedure_name)
print("Date:", procedure2.procedure_date)
print("Practitioner:", procedure2.practitioner_name)
print("Charge: $", procedure2.charges)
print()
# 1. procedure2.procedure_name accesses the procedure name stored in the first Procedure object. 
# 2. Python prints it along with the date, practitioner and charge

print("======= PROCEDURE 3 =======")
print("Procedure:", procedure3.procedure_name)
print("Date:", procedure3.procedure_date)
print("Practitioner:", procedure3.practitioner_name)
print("Charge: $", procedure3.charges)
print()
# 1. procedure3.procedure_name accesses the procedure name stored in the first Procedure object. 
# 2. Python prints it along with the date, practitioner and charge

# Step 7 Calculate total charges
total_charges = procedure1.charges + procedure2.charges + procedure3.charges
print("======= TOTAL CHARGES =======")
print("Total: $", total_charges)
# 1. Python accesses charges in each procedure object.
# 2. it adds them together using
# 3. The total is stored in total_charges
# 4. print displays the total amount of money for all procedures.

# How Python Reads this program
# 1. Python first defines the classes (Patient and Procedure)
# 2. It then executes the program creating objects.
# 3. It stores data inside objects using self.
# 4. When print statements are called, Python retrieves data from objects and displays it.
# 5. Arithmetic operations like adding charges are computed normally. 
