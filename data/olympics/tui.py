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
    print(f"""
    Please select one of the options:
    {"[years]":<10} List unique years
    {"[tally]":<10} Tally up medals
    {"[team]":<10} Tally up medals for each team
    {"[exit]":<10} Exit the menu
    
    """)
    tally = input("Your selection:")
    return tally.strip().lower()


def display_medal_tally(tally):
    print(f"| {'Gold'}:<10 | {tally['Gold']:<10} |")
    print(f"| {'Silver'}:<10 | {tally['Silver']:<10} |")
    print(f"| {'Bronze'}:<10 | {tally['Bronze']:<10} |")


def display_team_medal_tally(team_tally):
    for team, tally in team_tally.items():
        print(team)
        print(f"\tGold:{tally['Gold']}, Silver:{tally['Silver']}, Bronze:{tally['Bronze']}")


def display_years(years):
    sorted_years = sorted(years, reverse=True)
    for year in sorted_years:
        print(year)
