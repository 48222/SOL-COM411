# Ask user for brightness level
print("What level of brightness is required?")
brightness_desired = int(input())
print("Adjusting brightness...")

for brightness in range(2, brightness_desired + 1, 2):
    print(f"Beep's brightness level: {'*' * brightness}")
    print(f"Bop's brightness level: {'*' * brightness}")

print("Adjustments complete!")