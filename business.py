import random

# Class to store pertinent information about the album
class Vinyl:
    def __init__(self, album_Name, album_Artist, album_Genre, album_Year, album_Price):
        self.albumName = album_Name
        self.albumArtist = album_Artist
        self.albumGenre = album_Genre
        self.albumYear = album_Year
        self.albumPrice = int(album_Price)


class VinylCollection:
    def __init__(self):
        self.vinyls = []
    
    # Function to add album to the collection
    def add_vinyl(self):
        # Get input from the user for album details
        album_Name = input("Album Name: ")
        album_Artist = input("Album Artist: ")
        album_Genre = input("Genre: ")
        album_Year = input("Album Year: ")
        album_Price = float(input("Price: "))

        # Create a new Vinyl object with the provided details and add it to the collection
        vinyl = Vinyl(album_Name, album_Artist, album_Genre, album_Year, album_Price)
        self.vinyls.append(vinyl)
        print(f"{album_Name} ({album_Year}) by {album_Artist} added to collection.")
    
    # Function to view vinyl collection
    def view_collection(self):
        if not self.vinyls:
            print("No records in the collection\n")
            return
        print("\nVinyl Collection")
        for id, vinyl in enumerate(self.vinyls, start=1):
            print(f"{id}. {vinyl.albumName} ({vinyl.albumYear}) - {vinyl.albumArtist} [{vinyl.albumGenre}] | Price: ${vinyl.albumPrice:.2f}")

    # Function to view price data
    def view_price_data(self):
        if not self.vinyls:
            print("No records in the collection. Please add a record to gather price data.\n")
            return
        # Calculate total collection price and average record price
        total_collection_price = sum(vinyl.albumPrice for vinyl in self.vinyls)
        average_price = total_collection_price / len(self.vinyls)

        # Determine most & least expensive records
        most_expensive = max(self.vinyls, key=lambda vinyl: vinyl.albumPrice)
        least_expensive = min(self.vinyls, key=lambda vinyl: vinyl.albumPrice)

        print("\nPrice Data")
        print(f"Total Collection Price: ${total_collection_price:.2f}")
        print(f"Average Vinyl Price: ${average_price:.2f}")
        print(f"Most Expensive Vinyl: {most_expensive.albumName} ({most_expensive.albumYear}) by {most_expensive.albumArtist} - ${most_expensive.albumPrice:.2f}")
        print(f"Least Expensive Vinyl: {least_expensive.albumName} ({least_expensive.albumYear}) by {least_expensive.albumArtist} - ${least_expensive.albumPrice:.2f}")
    
    # Function to select a random record
    def select_random_vinyl(self):
        if not self.vinyls:
            print("No records in the collection\n")
            return
        random_vinyl = random.choice(self.vinyls)
        print(f"Randomly Selected Vinyl: {random_vinyl.albumName} ({random_vinyl.albumYear}) by {random_vinyl.albumArtist} [{random_vinyl.albumGenre}]\n")

