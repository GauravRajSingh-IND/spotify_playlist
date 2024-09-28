from scraper import BillBoard
from spotify import Spotify

# get the data of a given date.
year = str(input("Please enter the year: "))
month = str(input("Please enter the month: "))
day = str(input("Please enter the day: "))

# create date variable required by Billboard class.
date = f"{year}-{month}-{day}"

# create scraper object.
billboard = BillBoard(date=date)
spotify = Spotify()

# get songs data.
songs_data = billboard.scrape()
songs_data = billboard.get_songs(data=songs_data)
songs_names_list = songs_data[2]

top100_songs = {}
# get songs spotify ID.
for song in songs_names_list:

    #extrat ID of song.
    ID = spotify.get_song_id(song_name=song)
    track_data = spotify.get_track(song_ID=ID)

    # append the data to dictionary.
    top100_songs[song] = {"ID":ID, "track_data":track_data}

print(top100_songs)



