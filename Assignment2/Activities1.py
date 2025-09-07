#Create a program that asks users for their weight in pounds and their height in feet 
#and inches.Calculate and display their BMI.

print("Welcome to the BMI Calculator!")

print("\n")

weight = float(input("Enter your weight in pounds: "))
heightFeet = int(input("Enter your height - Feet: "))
heightInches = int(input("Enter your height - Inches: "))

totalHeightIn = (heightFeet * 12) + heightInches
heightMeter = totalHeightIn * 0.0254
weightKg = weight * 0.453592

bmi = weight /(heightMeter ** 2)

print(f"\nYour BMI is: {bmi:.1f}")

print("\nBMI Categories (WHO Reference):") 
print("Underweight   : BMI < 18.5")
print("Normal weight : 18.5 ≤ BMI < 25")
print("Overweight    : 25 ≤ BMI < 30")
print("Obese         : BMI ≥ 30")