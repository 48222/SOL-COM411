# My review programme
print("What is your favorite rock band>?")
band = input()
print(f"What is your favorite album of {band}?")
album = input()
if (band == "Rolling Stones") and (album == "Let it Bleed") or (album == "Sticky Fingers"):
    print(f"Great! {album} is one of my favorites as well!")
elif (band == "Led Zeppelin") and (album == "Coda"):
    print(f"I appreciate your decision, but I have a different taste, therefore I don't like {album}")
else:
    print(f"Great! Any {band} and {album} is fine with my, as long as it's music :D ")
