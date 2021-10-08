# Ask the user where to look
print("Where should I look?")
look = input()
if look == "In the bedroom":
    print("Where in the bedroom should I look?")
    bedroom = input()
    if bedroom == "Under the bed":
        print("Found some shoes but no battery")
    else:
        print("Found some mess but no battery")
# Bathroom
elif look == "In the bathroom":
    print("Where in the bathroom should I look?")
    bath = input()
    if bath == "In the bathtub":
        print("Found a rubber dyck but no battery")
    else:
        print("found a wet surface but no battery")
# Lab
elif look == "In the lab":
      print("Where in the lab should I look?")
      lab = input()
      if lab == "On the table":
          print("YES! I found my battery!")
      else:
          print("found some tools but no battery")
# End
else:
    print("I don't know where that is, but I will keep looking")
