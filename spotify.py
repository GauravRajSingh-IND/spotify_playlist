from dotenv import load_dotenv
import requests
import os

load_dotenv()

class Spotify:

    def __init__(self):

        self.client_id = os.getenv('spotify_client_id')
        self.client_secret = os.getenv('spotify_client_secret')
        self.access_token = None


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
            self.access_token = access_token
        else:
            self.access_token = None


