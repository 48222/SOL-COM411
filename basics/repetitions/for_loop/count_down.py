# Ask the user how far away they are from the cave
print("How far are we from the cave?")
distance = int(input())
for count in range(distance, 0, -1):
    print(f"{count} Steps Remaining")

print("We have reached the cave!")
