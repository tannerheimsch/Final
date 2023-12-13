from business import VinylCollection
import db


#region -- MENU ELEMENTS --
def display_title():
    print(" "*17 + "Vinyl Collection Tracker")

def display_separator_thick():
    print("=" *56)

def display_menu():
    print("\nMENU OPTIONS\n1 - Add Vinyl To Collection\n2 - View Collection\n3 - View Price Data\n4 - Select Random Vinyl\n5 - Import from CSV\n6 - Show Menu Options\n7 - Exit Program")
#endregion

#region -- MAIN FUNCTION
def main():
    vinyl_collection = VinylCollection()

    display_separator_thick()
    display_title()
    display_separator_thick()
    display_menu()

    while True:
        menu_option = int(input("Menu Option: "))
        if menu_option == 1:
            # Get the last added vinyl from the collection and add the vinyl to the database
            vinyl_collection.add_vinyl()
            added_vinyl = vinyl_collection.vinyls[-1]
            db.add_vinyl_to_db(added_vinyl.albumName, added_vinyl.albumArtist, added_vinyl.albumGenre,
                               added_vinyl.albumYear, added_vinyl.albumPrice)
        elif menu_option == 2:
                # Retrieve all vinyl from the database and update the collection
            vinyl_collection.vinyls = db.get_all_vinyls_from_db()
            vinyl_collection.view_collection()
        elif menu_option == 3:
            vinyl_collection.view_price_data()
        elif menu_option == 4:
            vinyl_collection.select_random_vinyl()
            # Import data from a CSV file into the database
        elif menu_option == 5:
            csv_file_name = input("Enter the name of the .csv file: ")
            db.import_csv_to_db(csv_file_name)
        elif menu_option == 6:
            display_menu()
        elif menu_option == 7:
            print("\nHappy listening. Goodbye! :)")
            break
        else:
            print("Invalid menu option. Please choose a valid option.")
    
#endregion

if __name__ == "__main__":
    main()