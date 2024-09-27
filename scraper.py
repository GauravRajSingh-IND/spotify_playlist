import requests
import bs4

class BillBoard:

    def __init__(self, date:str):

        self.url = "https://www.billboard.com/charts/hot-100/"
        self.date = date

    def get_endpoint(self):
        return f"{self.url}/{self.date}/"

    def scrape(self):

        # get the end_point url
        end_point = self.get_endpoint()

        try:
            response = requests.get(url=end_point)
            response.raise_for_status()
            return {"is_fetched":True, "response":response.text}
        except requests.RequestException as e:
            return {"is_fetched":False, "response":f"Error:{e}"}
