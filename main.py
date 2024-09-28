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

print(songs_ID)

data = ['2FQrifJ1N335Ljm3TjTVVf', '7221xIgOnuakPdLqT0F3nP', '6AI3ezQ4o3HUoP6Dhudph3', '2qSkIjg1o9h3YT9RAgYN75',
        '5AJ9hqTS2wcFQCELCFRO7A', '5N3hjp1WNayUPZrA8kJmJP', '4IadxL6BUymXlh8RCJJu7T', '6tNQ70jh4OwmPGpYy6R2o9',
        '6usohdchdzW9oML7VC4Uhk', '0WbMK4wrZ1wFSty9F7FCgu', '6dOtVTDdiauQNBQEDOtlAB', '7fveJ3pk1eSfxBdVkzdXZ0',
        '4ZJ4vzLQekI0WntDbanNC7', '2tudvzsrR56uom6smgOcSf', '2OzhQlSqBEmt7hmkYxfT6m', '2HYFX63wP3otVIvopRS99Z',
        '5ZLL6wYXeqg0k35ZkDRfhZ', '1bjeWoagtHmUKputLVyDxQ', '4KULAymBBJcPRpk1yO4dOG', '4pkb8SbRGeHAvdb87v9rpf',
        '2uqYupMHANxnwgeiXTZXzd', '0Izt8MdEU7zDy2hDsm5YkH', '00vR63trn1CzygcjgAFaiM', '2Zo1PcszsT9WQ0ANntJbID',
        '629DixmZGHc7ILtEntuiWE', '51ZQ1vr10ffzbwIjDCwqm4', '73KAidtqbDftZjy8AD0H04', '2hKYtHbwYOSjvYQhVdUpdQ',
        '76ODTQOl0JZQbhfxs6nRV9', '4xhsWYTOGcal8zt0J161CU', '0SdBkFh6u5IHIXqlBu0NyI', '6jlG8gBPNAgBgoivw2Ig09',
        '0mflMxspEfB0VbI1kyLiAv', '6GG4yyk3UATdBfTHVgI8PB', '0Aoq3irHJHWVtsnPs1HlH4', '0y5Ex8oQ8zCH5TQxHUy1Eo',
        '6XjDF6nds4DE2BBbagZol6', '6WatFBLVB0x077xWeoVc2k', '6WO7IDGLakjO38lsvI2gHB', '2MjXWroB9wlTG2kqv3avfS',
        '0wXThIDxO3YRJCpPgnmbkw', '3qhlB30KknSejmIvZZLjOD', '48X5k2vce5rXckgDAnXMsa', '3kMrazSvILsgcwtidZd1Qd',
        '3Vr3zh0r7ALn8VLqCiRR10', '0oZ1hEmIpbO3PzREe2HZeL', '1XBYiRV30ykHw5f4wm6qEn', '7FOgcfdz9Nx5V9lCNXdBYv', '3rUGC1vUpkDG9CZFHMur1t', '1t2MQpMDtJT5VL2tAPHrGN', '4y1LsJpmMti1PfRQV9AWWe', '2hrycoFU1mZw6YPvMcn8yC', '6sHsXIJoEN5JpdkGMQDJxt', '77DRzu7ERs0TX3roZcre7Q', '57wp7VFnV8X0pSVnYArGeJ', '1k2pQc5i348DCHwbn5KTdc', '29ZAW0BAp6O4C6fUncCjBk', '28drn6tQo95MRvO0jQEo5C', '72kGuWpRiuA149Bn5lDkIO', '1Ye5TcYtFsj0MiWHtR8eXt', '4o0lphbPt3npXyIQgSqY5S', '4sFnOjqO3s7Iphbg2MPKDd', '3ZP1AbM0rurWtqQIhTVcln', '59xD5osEFsaNt5PXfIKUnX', '7BRD7x5pt8Lqa1eGYC4dzj', '5ajntPJGa5UNKqJEbsAa93', '6saYisCUAZXc505blie9kZ', '5b3XJ1pjrHO5JtY2PcTjnI', '1vJCkmbu3YzIe6NjXS9BXX', '6vvPecFTmWxDfEJ6cYT1wa', '7iQMm50NNwlUIRWhONZR2k', '0e1KTuawmiFLiK0Lh3nNtM', '1C84d9abZVKWHT2YYpoean', '0hhzNPE68LWLfgZwdpxVdR', '4IFd7EVCyJsUHesBMXI8ju', '3Pbp7cUCx4d3OAkZSCoNvn', '2OUK5td58k4BV2GvFdfdzr', '65M92JpTbAdHmTQm4jGaDa', '2bl81llf715VEEbAx03yvB', '1TfqLAPs4K3s2rJMoCokcS', '3dj4wgM3cPeuLwMNHDuBon', '1kbEbBdEgQdQeLXCJh28pJ', '23bEisUvcSmIELLy4CMhkN', '2p8IUWQDrpjuFltbdgLOag', '3QaPy1KgI7nu9FJEQUgn6h', '4w2GLmK2wnioVnb5CPQeex', '3WSOUb3U7tqURbBSgZTrZX', '1kPhV0KQui1phEpjnWIqUN', '7FKAVg9SA7QYLxdVRLnKjd', '2ObBVRY8a2lnAkNG62u9eC', '1YvT4ml5LQM8ZYcLvqsAkD', '5uQ7de4EWjb3rkcFxyEOpu', '6w7OpHp3Y3ByHzmfQXYCRN', '11nmHJICkQ9emiYJJINygH', '4KWeGKChLKcnZsj3sIOSkW', '331l3xABO0HMr1Kkyh2LZq', '2d8UxVNhJinc8uat9PoM9y', '6fPan2saHdFaIHuTSatORv', '2YFhqZvhTpyK13gKXMKV7R', '1HbzxLqpNVPdiBXvpC7Ovb']