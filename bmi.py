# BMI-Calculator
print("This program is to calculate the BMI of an individual\n")
name=input("Enter your Name : ")
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

bmi = weight / height ** 2
print("Your BMI is: "+ str(bmi))
if bmi < 18.5:
    print("You are underweight.")
elif 18.5 <= bmi < 25:
    print("You have a normal weight.")
elif 25 <= bmi < 30:
    print("You are overweight.")
else:
    print("You are obese.")
    
