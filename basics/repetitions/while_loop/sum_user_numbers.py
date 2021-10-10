# Bop calculating sum
print("How many numbers should I sum up?")
numbers_to_sum = int(input())
summed = 0
print()
total = 0
while summed < numbers_to_sum:
    print(f"Please enter number {summed} of {numbers_to_sum}:")
    number = int(input())
    total = total + number
    summed = summed + 1
# End
print(f"The answer is {total}")


