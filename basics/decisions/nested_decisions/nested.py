# ask what type of cover book has
print("what type of cover does the book have? (Soft/Hard)")
book_cover = input()
if book_cover == "soft":
    print("is the book perfect bound? (Yes/No)")
    perfect_bound = input()
    if perfect_bound == "yes":
        print("Soft cover, perfect bound books are very popular!")
    else:
        print("Soft covers with coils or stitches are great for short books")
elif book_cover == "hard":
    print("Books with hard covers can be more expensive!")
