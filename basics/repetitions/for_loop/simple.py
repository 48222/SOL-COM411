# Ask the user how many mountains to display
print("How many mountains should I display?")
mountains = int(input())
print("Displaying...")
for count in range(mountains):
    print("""
             __
            /  \\_  
           /^    \\
          /  ^    \\_
        _/ ^ ^     ^\\
       /  ^     ^    \\

    """)
