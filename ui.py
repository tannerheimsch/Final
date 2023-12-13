from business import Vinyl, VinylCollection
#from db import VinylDatabase

#region -- MENU ELEMENTS --
def display_title():
    print(" "*17 + "Vinyl Collection Tracker")

def display_separator_thick():
    print("=" *56)

def display_separator_thin():
    print("-" *70)

def display_menu():
    print("\nMENU OPTIONS\n1 - Add Vinyl to Collection\n2 - View Collection\n3 - View Price Data\n4 - Select Random Vinyl\n5 - Show Menu Options\n6 - Exit Program")


#endregion

#region -- MAIN FUNCTION
def main():
    vinyl_collection = VinylCollection()
    #vinyl_database = VinylDatabase()

    display_separator_thick()
    display_title()
    display_separator_thick()
    display_menu()

    while True:
        menu_option = int(input("Menu Option: "))
        if menu_option == 1:
            vinyl_collection.add_vinyl()
        elif menu_option == 2:
            vinyl_collection.view_collection()
        elif menu_option == 3:
            vinyl_collection.view_price_data()
        elif menu_option == 4:
            vinyl_collection.select_random_vinyl()
        elif menu_option == 5:
            display_menu()
        elif menu_option == 6:
            break
        else:
            print("Invalid menu option. Please choose a valid option.")


#endregion

if __name__ == "__main__":
    main()