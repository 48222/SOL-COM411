# Start of the program
print("Program Started")
print("Please enter a standard character")
character = input()
if len(character) == 1:
    print(f"The ASCII code for {character} is {ord(character)}")
else:
    print("A single standard character was expected")

print("Program ended.")