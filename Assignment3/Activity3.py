# Ravindra Tantuwaya
# Session 3 - Conditions 
# BMI Calculator with proper constants, validation, and structured functions

# 1. Define Constants for unit conversion
INCHES_PER_FOOT = 12
METERS_PER_INCH = 0.0254
KILOGRAMS_PER_POUND = 0.453592


# 2. Define the Function for weight
def get_valid_weight():
 
    try:
        weight = float(input("Enter your weight in pounds: "))
    except ValueError:
        raise ValueError("Invalid input. Please enter a numeric value for weight.")

    if weight <= 0 or weight > 1000:
        raise ValueError("Weight must be between 1 and 1000 pounds.")

    return weight


# 3. Define the Function for height (feet)
def get_valid_height_feet():
 
    try:
        heightFt = int(input("Enter your height - Feet: "))
        if heightFt <= 0 or heightFt > 8:
            raise Exception("Height in feet must be between 1 and 8.")
        return heightFt
    except ValueError:
        raise ValueError("Please enter a whole number for feet.")
    except Exception as e:
        raise Exception(f"Invalid height (feet) input: {e}")


# 4. Define the Function for height (inches)
def get_valid_height_inches():
 
    try:
        heightIn = int(input("Enter your height - Inches: "))
        if heightIn < 0 or heightIn >= 12:
            raise Exception("Height in inches must be between 0 and 11.")
        return heightIn
    except ValueError:
        raise ValueError("Please enter a whole number for inches.")
    except Exception as e:
        raise Exception(f"Invalid height (inches) input: {e}")


# 5. Define the Function to calculate BMI
def calculatorBMI(weightLbs, heightFt, heightIn):
  
    totalHeightIn = (heightFt * INCHES_PER_FOOT) + heightIn
    heightMeter = totalHeightIn * METERS_PER_INCH
    weightKg = weightLbs * KILOGRAMS_PER_POUND
    bmi = weightKg / (heightMeter ** 2)
    return bmi


# 6. Main Program Execution
print("Welcome to the BMI Calculator!\n")

try:
    # Get valid inputs
    weight = get_valid_weight()
    heightFeet = get_valid_height_feet()
    heightInches = get_valid_height_inches()

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

except ValueError as ve:
    print(f"\nValue Error: {ve}")
except TypeError as te:
    print(f"\nType Error: {te}")
except Exception as e:
    print(f"\nGeneral Error: {e}")
