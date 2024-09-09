# class DataManager:
#     #This class is responsible for talking to the Google Sheet.
#     pass

import requests
import pandas as pd
from requests.structures import CaseInsensitiveDict

class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        # self.endpoint = "https://api.sheety.co/db576b61a317675d114004c8294a6961/flightDeals/prices"
        APIKEYS = "1Hp-IyasXdwEKAkVj_5PHjAZomEIeBv69j9uTCWGWZMw"
        # header = {
        #     "x-app-id" : APPID, 
        #     "x-app-key" : APIKEYS,
        #     "Content-Type": "application/json",
        #     "Authorization": "Bearer somerandomebearertoken123."
        # }
        self.endpoint = "https://api.sheety.co/db576b61a317675d114004c8294a6961/flightDeals/prices"
        # tequilla_endpoint = "https://api.tequila.kiwi.com/"
        # tequilla_header = {
        #     'apikey': '2Zc583pgrksLuGUf-3jTz9cuIu7nJI03'
        # }

        # Fetch data from Sheety API
        sheet_response = requests.get(self.endpoint).json()
      
        # Create DataFrame from the response
        df = pd.DataFrame(sheet_response['prices'])
    
        # Iterate over cities in the DataFrame
        rowid = 2
        for city in df['city']:
            locations_api = "locations/query"
            tequilla_params = {
                'term': city  # Use 'term' key to specify the city name
            }
            # Make Tequila API request
            json_data = requests.get(tequilla_endpoint + locations_api, params=tequilla_params, headers=tequilla_header).json()
            iata_code =json_data['locations'][0]['code']  # Corrected to access the 'locations' key
            put_url = sheet_endpoint + "/" + str(rowid)  # Assuming 'objectId' is a valid column in your DataFrame
            new_data = {
                        "price": {
                            "iataCode": iata_code
                        }
                    }
            response = requests.put(
                        url=put_url,
                        json=new_data
                    )
            rowid+=1
            
    def get_data(self):
        headers = CaseInsensitiveDict()
        headers["Accept"] = "application/json"
        response = requests.get(self.endpoint, headers=headers)
        response.raise_for_status()
        return response.json()["prices"]

    def update_data(self, row_id, data):
        headers = CaseInsensitiveDict()
        headers["Content-Type"] = "application/json"
        # headers["Authorization"] = "Bearer your_token"
        endpoint = f"{self.endpoint}/{row_id}"
        response = requests.put(endpoint, headers=headers, json=data)
        response.raise_for_status()


# steps for initialising Sheet with IATA CODE
"""
1. get city code
2. search for city code
3. update city code in relevant row
"""