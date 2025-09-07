# Ravindra Tantuwaya
# Lesson 2 - Functions
# Group Assignment 1
# Define constants for height and weight conversions and use the self-documenting function, 
# variable, and constant names

#1. Define Constants for unit conversion
#   The computer stores these value in memory as constants
INCHES_PER_FOOT = 12
METERS_PER_INCH = 0.0254
KILOGRAMS_PER_POUND = 0.453592

#2. Define the Function
    # It stores the function in memory
def calculatorBMI(weightLbs, heightFt, heightIn): 
    totalHeightIn = (heightFt * INCHES_PER_FOOT) + heightIn  # Convert height to total inches
    heightMeter = totalHeightIn * METERS_PER_INCH # Convert height to meters
    weightKg = weightLbs * KILOGRAMS_PER_POUND   # Convert weight to kilograms
    bmi = weightKg /(heightMeter ** 2) # Calculate BMI using the metric formula
    return bmi

#3. Execute main code
    # This prints the welcome message to the screen
print("Welcome to the BMI Calculator!")
print("\n")

#4. Take User input
    # Shows prompts to the user and wait for the user to type input
    # Store it in memory as variable  
weight = float(input("Enter your weight in pounds: "))
heightFeet = int(input("Enter your height - Feet: "))
heightInches = int(input("Enter your height - Inches: "))

#5. Call the Function
    # Function bmiResult passes the 3 values from the user
    # the calculated BMI in function
    # Retrun the bmi 
    # Store in bmiResult
bmiResult = calculatorBMI(weight, heightFeet, heightInches)  

#6 Display the Result
   # bmiResult
print(f"\nYour BMI is: {bmiResult:.1f}")  

# Display the standard BMI categories
print("\nBMI Categories (WHO Reference):")  
print("Underweight   : BMI < 18.5")
print("Normal weight : 18.5 ≤ BMI < 25")
print("Overweight    : 25 ≤ BMI < 30")
print("Obese         : BMI ≥ 30")