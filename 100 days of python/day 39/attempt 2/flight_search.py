import requests
import os
from dotenv import load_dotenv, find_dotenv
dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

TEQUILA_API_KEY = os.getenv('TEQUILA_API_KEY')
tequila_endpoint = "https://api.tequila.kiwi.com"
location_query = "/locations/query"
header = {
    "apikey" : TEQUILA_API_KEY
}

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    
    def get_iata_code(self, city):
        params = {
            "term" : city,
        }
        response = requests.get(tequila_endpoint+location_query, params=params, headers=header)
        return response.json()['locations'][0]['code']

    pass






    