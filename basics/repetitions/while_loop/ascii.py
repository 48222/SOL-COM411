# Beep avoid live cables
print("How many bars should be charged?")
bars = int(input())
bars_charged = 0
print()
while bars_charged < bars:
    bars_charged = bars_charged + 1
    print(f"Charging: {'█'* bars_charged}")
print("The battery is fully charged.")
