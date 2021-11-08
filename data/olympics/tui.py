def started(msg=""):
    print("-------------------------------------------------------------------------------------")
    print(f"Operation Started:{msg}...\n")


def completed():
    print("")
    print("Operation completed.")
    print("-------------------------------------------------------------------------------------")


def error(msg):
    print(f"Error! {msg}")


def menu():
    print("""
    Please select one of the options:
    [years] List unique years
    [tally] Tally up medals
    [team] Tally up medals for each team
    [exit[ Exit the menu
    
    """)
    print("Your selection:")
    tally = int(input())
    return tally


def display_medal_tally(tally):
    tally = {"Gold": 10, "Silver": 5, "Bronze": 2}
    print(f"")