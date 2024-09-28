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

"""
['3y2cIKLjiOlp1Np37WiUdH', '246dkjvS1zLTtiykXe5h60', '2YZyLoL8N0Wb9xBt1NhZWg', '74KM79TiuVKeVCqs8QtB0B',
 '1WaFQSHVGZQJTbf0BdxdNo', '74KM79TiuVKeVCqs8QtB0B', '2FXC3k01G6Gw61bmprjgqS', '22wbnEMDvgVIAGdFeek6ET',
  '33qOK5uJ8AR2xuQQAhHump', '7GlBOeep6PqTfFi59PTUUN', '6qqNVTkY8uBg9cP3Jd7DAH', '4oUHIQIBe0LHzYfvXNW4QM', 
  '40ZNYROS4zLfyyBSs2PGe2', '1RyvyyTE3xzB2ZywiAwp0i', '06HL4z0CvFAxyc27GXpf02', '7dGJo4pcD2V6oG8kP0tJRR',
  '246dkjvS1zLTtiykXe5h60', '7tYKF4w9nC0nq9CsPZTHyP', '40ZNYROS4zLfyyBSs2PGe2', '64KEffDW9EtZ1y2vBYgq8T', '7Ez6lTtSMjMf2YSYpukP1I',
  '2qoQgPAilErOKCwE2Y8wOG', '3tJoFztHeIJkJWMrx0td2f', '74KM79TiuVKeVCqs8QtB0B', '6qqNVTkY8uBg9cP3Jd7DAH', '66CXWjxzNUsdJxJ2JdwvnR',
  '1Tie3AZgLQZqYEp8Fv4zOZ', '2qoQgPAilErOKCwE2Y8wOG', '19k8AgwwTSxeaxkOuCQEJs', '2LIk90788K0zvyj2JJVwkJ', '2qoQgPAilErOKCwE2Y8wOG', 
  1WaFQSHVGZQJTbf0BdxdNo', '2RQXRUsr4IW1f3mKyKsy4B', '718COspgdWOnwOFpJHRZHS', '7GT8mZHoTsRGMkmownzCeo', '6BRxQ8cD3eqnrVj6WKDok8',
   '7CvTknweLr9feJtRGrpDBy', '790FomKkXshlbRYZFtlgla', '22wbnEMDvgVIAGdFeek6ET', '3DbwFQlvLxRSi2uX8mf81A', '3win9vGIxFfBRag9S63wwf', '5p9HO3XC5P3BLxJs5Mtrhm', '6zLBxLdl60ekBLpawtT63I', '3K2zB87GZv1krx031en5VA', '3bO19AOone0ubCsfDXDtYt', '5H4yInM5zmHqpKIoMNAx4r', '2tIP7SsRs7vjIcLrU85W8J', '7GlBOeep6PqTfFi59PTUUN', '45dkTj5sMRSjrmBSBeiHym', '3RqBeV12Tt7A8xH3zBDDUF', '2BTZIqw0ntH9MvilQ3ewNY', '0jPHHnU8GUWEF7rwPE9osY', '05oH07COxkXKIMt6mIPRee', '2YZyLoL8N0Wb9xBt1NhZWg', '2EMAnMvWE2eb56ToJVfCWs', '7GlBOeep6PqTfFi59PTUUN', '06HL4z0CvFAxyc27GXpf02', '1RyvyyTE3xzB2ZywiAwp0i', '0ChjBYedhZTQnWZWQYg15U', '4sGi5splC7qJ8Nr2ctP7X6', '3K8o5pKBLJYPbxu4AT4aqH', '4nDoRrQiYLoBzwC5BhVJzF', '3TQ9JTBI2n2hfo7aRONEYV', '6M2wZ9GZgrQXHCFfjv46we', '6qqNVTkY8uBg9cP3Jd7DAH', '3DbwFQlvLxRSi2uX8mf81A', '181bsRPaVXVlUKXrxwZfHK', '181bsRPaVXVlUKXrxwZfHK', '4sCKpwwEsgReZxjtKFm2A0', '5L1lO4eRHmJ7a0Q6csE5cT', '4sCKpwwEsgReZxjtKFm2A0', '39af15p0feaAOdL9DTRj3m', '0pePYDrJGk8gqMRbXrLJC8', '4tuJ0bMpJh08umKkEXKUI5', '0YinUQ50QDB7ZxSCLyQ40k', '4j96cMcT8GRi11qbvo1cLQ', '181bsRPaVXVlUKXrxwZfHK', '4YLtscXsxbVgi031ovDDdh', '4tuJ0bMpJh08umKkEXKUI5', '0NKDgy9j66h3DLnN8qu1bB', '33qOK5uJ8AR2xuQQAhHump', '06HL4z0CvFAxyc27GXpf02', '3FfvYsEGaIb52QPXhg4DcH', '1Xyo4u8uXC1ZmMpatF05PJ', '6qqNVTkY8uBg9cP3Jd7DAH', '25uiPmTg16RbhZWAqwLBy5', '7GlBOeep6PqTfFi59PTUUN', '1oSPZhvZMIrWW5I41kPkkY', '19k8AgwwTSxeaxkOuCQEJs', '6x2LnllRG5uGarZMsD4iO8', '718COspgdWOnwOFpJHRZHS', '11p2E654TTU8e0nZWBR4AL', '6tPHARSq45lQ8BSALCfkFC', '3win9vGIxFfBRag9S63wwf', '7dGJo4pcD2V6oG8kP0tJRR', '1Cs0zKBU1kc0i8ypK3B9ai', '06HL4z0CvFAxyc27GXpf02', '6qqNVTkY8uBg9cP3Jd7DAH', '25uiPmTg16RbhZWAqwLBy5', '6IKlXZEFOvk9itrP1s0knJ']"""