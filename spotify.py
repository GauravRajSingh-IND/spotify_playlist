from http.client import responses

from dotenv import load_dotenv
import requests
import os

load_dotenv()

class Spotify:

    def __init__(self):

        self.client_id = os.getenv('spotify_client_id')
        self.client_secret = os.getenv('spotify_client_secret')
        self.access_token = self.get_access_token()


    def get_access_token(self):
        # Step 1: Set up the token request
        auth_url = 'https://accounts.spotify.com/api/token'

        auth_data = {
            'grant_type': 'client_credentials',
            'client_id': self.client_id,
            'client_secret': self.client_secret,
                    }

        # Step 2: Make the POST request
        response = requests.post(auth_url, data=auth_data)

        # Step 3: Parse the response
        if response.status_code == 200:
            access_token = response.json()['access_token']
            return access_token
        else:
            return None

    def get_song_id(self, song_name):

        search_url = f'https://api.spotify.com/v1/search?q={song_name}&type=track'

        headers = {
            'Authorization': f'Bearer {self.access_token}'
        }

        try:
            response = requests.get(search_url, headers=headers)

            if response.status_code == 200:
                return response.json()['tracks']['items'][0]['id']
            else:
                return None
        except requests.RequestException as e:
            return f"Error searching for song: {response.status_code} - {response.text}"

    def get_track(self, song_ID:str):

        search_url = f"https://api.spotify.com/v1/tracks/{song_ID}"

        headers = {
            'Authorization': f'Bearer {self.access_token}'
        }

        params = {
            "id":song_ID,
        }

        try:
            response = requests.get(search_url, headers=headers)

            if response.status_code == 200:
                return response.json()
            else:
                return None
        except requests.RequestException as e:
            return f"Error searching for song: {response.status_code} - {response.text}"
