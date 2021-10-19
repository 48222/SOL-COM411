# Defining the function
def climb_ladder(remaining, crossed):
    if remaining > crossed:
        print("Still some way to go!")
    else:
        print("We are almost there!")


# Call the function

climb_ladder(5, 2)
climb_ladder(2, 5)
