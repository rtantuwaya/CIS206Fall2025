# a test plan for the BMI program. 

from bmi_functions import calculatorBMI, calculatorBMI_inches

def test_calculatorBMI():
    bmi = calculatorBMI(150, 5, 10)
    assert round(bmi, 1) == 21.5

def test_calculatorBMI_inches():
    bmi = calculatorBMI_inches(150, 70)
    assert round(bmi, 1) == 22.5
