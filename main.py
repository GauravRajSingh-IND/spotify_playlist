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

songs_ID = []
# get songs spotify ID.
for song in songs_names_list:

    #extrat ID of song.
    songs_ID.append(spotify.get_song_id(song_name=song))

