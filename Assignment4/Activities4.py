# Ravindra Tantuwaya
# Session 4 - Loops 
# BMI Calculator with proper constants, validation, and Reusable Functions Using Loops

# 1. Define Constants for unit conversion
INCHES_PER_FOOT = 12
METERS_PER_INCH = 0.0254
KILOGRAMS_PER_POUND = 0.453592


# 2. Define the Function for weight
def get_valid_weight():
   
    while True:
        try:
            weight = float(input("Enter your weight in pounds: "))
            if weight <= 0 or weight > 1000:
                raise ValueError("Weight must be between 1 and 1000 pounds.")
            return weight
        except ValueError as ve:
            print(f"{ve}")
   

# 3. Define the Function for height (feet)
def get_valid_height_feet():

    while True:
        try:
            heightFt = int(input("Enter your height - Feet: "))
            if heightFt <= 0 or heightFt > 8:
                raise Exception("Height in feet must be between 1 and 8.")
            return heightFt
        except ValueError:
            print("ValueError: Please enter a whole number for feet.")
        except Exception as e:
            print(f"Exception: Invalid height (feet) input: {e}")

# 4. Define the Function for height (inches)
def get_valid_height_inches():
    while True:
        try:
            heightIn = int(input("Enter your height - Inches: "))
            if heightIn < 0 or heightIn >= 12:
                raise Exception("Height in inches must be between 0 and 11.")
            return heightIn
        except ValueError:
            print("Please enter a whole number for inches.")
        except Exception as e:
            print(f"Invalid height (inches) input: {e}")


# 5. Define the Function to calculate BMI
def calculatorBMI(weightLbs, heightFt, heightIn):
  
    totalHeightIn = (heightFt * INCHES_PER_FOOT) + heightIn
    heightMeter = totalHeightIn * METERS_PER_INCH
    weightKg = weightLbs * KILOGRAMS_PER_POUND
    bmi = weightKg / (heightMeter ** 2)
    return bmi

# 6. Define the Function to calculate BMI inches

def calculatorBMI_inches(weightLbs, totalHeightInches):
    heightMeter = totalHeightInches * METERS_PER_INCH
    weightKg = weightLbs * KILOGRAMS_PER_POUND
    bmi = weightKg / (heightMeter ** 2)
    return bmi

# 7. Define the Function for Displays a formatted BMI table with:
def display_bmi_table():
    print("\nBMI Table (Weight vs. Height)\n")
    print("Weight \\ Height", end="\t")
    for height in range(58, 77, 2):
        print(f"{height}\"", end="\t")
    print()

    for weight in range(100, 251, 10):
        print(f"{weight} lb", end="\t\t")
        for height in range(58, 77, 2):
            bmi = calculatorBMI_inches(weight, height)
            print(f"{bmi:.1f}", end="\t")
        print()
 


# 8. Main Program Execution
print("Welcome to the BMI Calculator!\n")


while True:
     print("\nChoose an option:")
     print("1. Calculate my BMI")
     print("2. View BMI Table")
     print("3. Quit")
     choice = input("Enter 1, 2, or 3: ").strip()
     
        # Get valid inputs
     if choice == '1':
         print("\nBMI Calculation")
         weight = get_valid_weight()
         #if weight is None:
            #break
         heightFeet = get_valid_height_feet()
         #if heightFeet is None:
          #  break
         heightInches = get_valid_height_inches()
         #if heightInches is None:
          #  break

    # Calculate BMI
         bmiResult = calculatorBMI(weight, heightFeet, heightInches)

    # Display the result
         print(f"\nYour BMI is: {bmiResult:.1f}")

    # Display BMI categories
         print("\nBMI Categories (WHO Reference):")
         print("Underweight   : BMI < 18.5")
         print("Normal weight : 18.5 ≤ BMI < 25")
         print("Overweight    : 25 ≤ BMI < 30")
         print("Obese         : BMI ≥ 30")

         if bmiResult < 18.5:
            category = "Underweight"
         elif bmiResult < 25:
            category = "Normal weight"
         elif bmiResult < 30:
            category = "Overweight"
         else:
           category = "Obese"

         print(f"\nYou are categorized as: {category}")

     elif choice == '2':
         display_bmi_table()

     elif choice == '3':
         print("Exit")
         break

     else:
         print(" Invalid option. Please enter 1, 2, or 3")

   

  
