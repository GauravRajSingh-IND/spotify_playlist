import re
import requests
from bs4 import BeautifulSoup


class BillBoard:

    def __init__(self, date:str):

        self.url = "https://www.billboard.com/charts/hot-100/"
        self.date = date
        self.is_success = True

    def get_endpoint(self):
        return f"{self.url}/{self.date}/"

    def scrape(self):

        # get the end_point url
        end_point = self.get_endpoint()

        try:
            response = requests.get(url=end_point)
            response.raise_for_status()
            return response
        except requests.RequestException as e:
            self.is_success = False

    def get_songs(self, data):

        soup = BeautifulSoup(data.text, "html.parser")

        songs_html = soup.find_all("div", class_="o-chart-results-list-row-container")

        songs_image = [song.find("img")['src'] for song in songs_html]
        songs_rank = [song.find("span").text.strip() for song in songs_html]
        songs_title = [song.find("h3").text.strip() for song in songs_html]

        return songs_image, songs_rank, songs_title





