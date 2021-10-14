# Ask user for markings
print("What strange markings do you see?")
markings = input()
print("Identifying...")

for count in range(0, len(markings), 1):
    print(f"index {count}:", markings[count])

