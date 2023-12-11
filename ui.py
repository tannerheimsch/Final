#region -- MENU ELEMENTS --
def display_title():
    print(" "*17 + "Vinyl Collection Tracker")

def display_separator_thick():
    print("=" *56)

def display_separator_thin():
    print("-" *70)

def display_menu():
    print("\nMENU OPTIONS")
    print("1 - Add Vinyl To Collection")
    print("2 - View Collection")
    print("3 - View Price Data")
    print("4 - Select Random Vinyl")
    print("5 - Show Menu Options")
    print("6 - Exit Program")

#endregion

#region -- MAIN FUNCTION
def main():
    display_separator_thick()
    display_title()
    display_separator_thick()
    display_menu()

#endregion

if __name__ == "__main__":
    main()