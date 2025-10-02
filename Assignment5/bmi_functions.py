# a test plan for the BMI program. 

INCHES_PER_FOOT = 12
METERS_PER_INCH = 0.0254
KILOGRAMS_PER_POUND = 0.453592

def calculatorBMI(weightLbs, heightFt, heightIn):
    totalHeightIn = (heightFt * INCHES_PER_FOOT) + heightIn
    heightMeter = totalHeightIn * METERS_PER_INCH
    weightKg = weightLbs * KILOGRAMS_PER_POUND
    bmi = weightKg / (heightMeter ** 2)
    return bmi

def calculatorBMI_inches(weightLbs, totalHeightInches):
    heightMeter = totalHeightInches * METERS_PER_INCH
    weightKg = weightLbs * KILOGRAMS_PER_POUND
    bmi = weightKg / (heightMeter ** 2)
    return bmi
