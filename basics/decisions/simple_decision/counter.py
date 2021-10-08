# Asking the user for a number
print("please enter the first number")
number1 = int(input())
print("please enter the second number")
number2 = int(input())
print("please enter the third number")
number3 = int(input())

even_numbers = 0
odd_numbers = 0

# odd or even
if number1 % 2 == 0:
    even_numbers = even_numbers + 1
else:
    odd_numbers = odd_numbers + 1
if number2 % 2 == 0:
    even_numbers = even_numbers + 1
else:
    odd_numbers = odd_numbers + 1
if number3 % 2 == 0:
    even_numbers = even_numbers + 1
else:
    odd_numbers = odd_numbers + 1

# display result
print(f"there were {even_numbers} even numbers and {odd_numbers} odd numbers.")
