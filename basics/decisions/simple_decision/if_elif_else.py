# Elif
print("Towards which direction should I print? (Up, Down, Left or Right)")
direction = input()
if direction == "up":
    print("I am painting in the upward direction.")
elif direction == "down":
    print("I am painting in the downward direction.")
elif direction == "left":
    print("I am painting in the left direction.")
elif direction == "right":
    print("I am painting in the right direction.")
else:
    print("Please choose a direction! (Up, Down, Left or Right)")
print("Painted in the chosen direction.")