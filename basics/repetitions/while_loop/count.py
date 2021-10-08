# Live Cables
print("How many live cables must I avoid?")
live_cables_to_avoid = int(input())
live_cables_avoided = 0
print()
while  live_cables_avoided < live_cables_to_avoid:
    print("Avoiding...", end="")
    live_cables_avoided = live_cables_avoided +1
    print(f"...Done! {live_cables_avoided} live cables avoided")
