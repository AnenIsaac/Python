# class DataManager:
#     #This class is responsible for talking to the Google Sheet.
#     pass

import requests
from requests.structures import CaseInsensitiveDict

class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.endpoint = "https://api.sheety.co/your_api_endpoint"

    def get_data(self):
        headers = CaseInsensitiveDict()
        headers["Accept"] = "application/json"
        response = requests.get(self.endpoint, headers=headers)
        response.raise_for_status()
        return response.json()["prices"]

    def update_data(self, row_id, data):
        headers = CaseInsensitiveDict()
        headers["Content-Type"] = "application/json"
        headers["Authorization"] = "Bearer your_token"
        endpoint = f"{self.endpoint}/{row_id}"
        response = requests.put(endpoint, headers=headers, json=data)
        response.raise_for_status()
