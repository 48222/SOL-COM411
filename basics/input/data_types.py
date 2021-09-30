# calculate BMI
print("What is your name human?")
name = input()
print("How old are you (in years)?")
age = input()
print("How tall are you (in meters)?")
height = float(input())
print("How much do you weight (in kilograms)?")
weight = int(input())
bmi = weight/height**2
print(f"{name} you are {age} years old and your BMI is {bmi:.2f}")
