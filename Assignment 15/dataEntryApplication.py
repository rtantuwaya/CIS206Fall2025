# Data Entry Application Using Tkinter

# This program demonstrates a Tkinter based data entry form that collects a first name, 
# last name, and a numeric value. It validates the numeric input and displays a popup error message 
# if the user enters a non-numeric value. When the button is clicked, the program processes 
# the input by converting the full name to uppercase and doubling the numeric value. 
# After completing these operations, the results are displayed directly on the form for the user to see.

# Step 1 
# Python imports Tkinter 
import tkinter as tk
# This loads the Tkinter GUI library, tkinter is renamed as tk for convenience.
from tkinter import messagebox
# messagebox is imported so popup windows can be displayed.


# Step 2
# Python creates the main window (the form)
window = tk.Tk()
#tk.Tk() creates the main application window.
window.title("Data Entry Application")
# .title() sets the window title.
window.geometry("950x300")
# .geometry() sets the size of the form.

# Step 3 
# Python configures the grid layout
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=1)
window.columnconfigure(3, weight=1)
# This tells Tkinter that all four columns in the window 

# Step 4. 
# Python creates labels and entry boxes

# First name
l1 = tk.Label(window, text="Enter your first name:", font=("Arial", 12))
l1.grid(column=0, row=0, padx=10, pady=10, sticky="w")

txt1 = tk.Entry(window, width=25, font=("Arial", 12))
txt1.grid(column=1, row=0)

# Last name
l2 = tk.Label(window, text="Enter your last name:", font=("Arial", 12))
l2.grid(column=2, row=0, padx=10, pady=10, sticky="w")

txt2 = tk.Entry(window, width=25, font=("Arial", 12))
txt2.grid(column=3, row=0)

# Numeric field
num_label = tk.Label(window, text="Enter a number for doubled:", font=("Arial", 12))
num_label.grid(column=0, row=1, padx=10, pady=10, sticky="w")

num_entry = tk.Entry(window, width=25, font=("Arial", 12))
num_entry.grid(column=1, row=1)

# Step 5.
# Result label is created
result_label = tk.Label(window, text="", font=("Arial", 12))
result_label.grid(column=0, row=3, columnspan=4, pady=20)


# Step 6
# Python defines the function
def process_data():
    first = txt1.get()
    last = txt2.get()
    number_text = num_entry.get()

    # Validate numeric input
    try:
        number = float(number_text)
    except ValueError:
        messagebox.showerror("Invalid Input", "ERROR: You must enter a numeric value!")
        return  # stop here

    # String manipulation
    full_name = (first + " " + last).upper()

    # Calculation
    doubled = number * 2

    # Show results
    result_label.config(
        text=f"Welcome Your Full Name in Uppercase: {full_name}\n"
             f"Doubled Number: {doubled}"
    )

# BUTTON
bt = tk.Button(window, text="Process", bg="orange", fg="green", command=process_data, font=("Arial", 12))
bt.grid(column=3, row=1, padx=10, pady=10)

# RUN APPLICATION
window.mainloop()
