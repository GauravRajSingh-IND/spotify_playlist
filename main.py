from scraper import BillBoard

# get the data of a given date.
year = str(input("Please enter the year: "))
month = str(input("Please enter the month: "))
day = str(input("Please enter the day: "))

# create date variable required by Billboard class.
date = f"{year}-{month}-{day}"

# create scraper object.
billboard = BillBoard(date=date)

# get songs data.
songs_data = billboard.scrape()
songs_data = billboard.get_songs(data=songs_data)
