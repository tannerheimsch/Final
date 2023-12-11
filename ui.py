#region -- MENU ELEMENTS --
def display_title():
    print(" "*17 + "Vinyl Collection Tracker")

def display_separator_thick():
    print("=" *56)

def display_separator_thin():
    print("-" *70)

def display_menu():
    print("\nMENU OPTIONS\n1 - Add Vinyl To Collection\n2 - View Collection\n3 - View Price Data\n4 - Select Random Vinyl\n5 - Show Menu Options\n6 - Exit Program")


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