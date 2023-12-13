import sqlite3
import csv
import os
from contextlib import closing
from business import Vinyl

DATABASE = "Final.sqlite"  # Database Name

# Function to establish database connection
def connect():
    return sqlite3.connect(DATABASE)

# Function to close database connection
def close(connection):
    connection.close()

# Function to create database table if not already created
def create_table():
    with closing(connect().cursor()) as cursor:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS vinylCollection (
                albumID INTEGER PRIMARY KEY AUTOINCREMENT,
                albumName TEXT NOT NULL,
                albumArtist TEXT NOT NULL,
                albumGenre TEXT NOT NULL,
                albumYear TEXT NOT NULL,
                albumPrice REAL NOT NULL
            );
        ''')

# Function to add vinyl to the database
def add_vinyl_to_db(album_Name, album_Artist, album_Genre, album_Year, album_Price):
    connection = connect()
    try:
        with closing(connection.cursor()) as cursor:
            cursor.execute('''
                INSERT INTO vinylCollection (albumName, albumArtist, albumGenre, albumYear, albumPrice)
                VALUES (?, ?, ?, ?, ?);
            ''', (album_Name, album_Artist, album_Genre, album_Year, album_Price))
        connection.commit()  # Commit changes to the database
    except Exception as e:
        print(f"Error adding vinyl to the database: {e}")
    finally:
        close(connection)

# Function to query database for vinyl and then add them to the vinyl list using the Vinyl class
def get_all_vinyls_from_db():
    with closing(connect().cursor()) as cursor:
        cursor.execute('''
            SELECT * FROM vinylCollection;
        ''')
        records = cursor.fetchall()
        vinyls = [Vinyl(*record[1:]) for record in records]  # Exclude the first element (albumID)
        return vinyls
    
# Function to import collection information from a .CSV (specifically a Discogs export)
def import_csv_to_db(csv_file_name):
    csv_file_path = os.path.join(os.getcwd(), csv_file_name)
    try:
        with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
            csv_reader = csv.DictReader(csvfile)
            for row in csv_reader:
                # Extract relevant information from the CSV columns
                artist = row.get('Artist', '')
                title = row.get('Title', '')
                released = row.get('Released', '')

                # Add the extracted information to the database
                add_vinyl_to_db(title, artist, '', released, '')
    except Exception as e:
        print(f"Error importing data from CSV: {e}")