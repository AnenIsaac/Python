import flight_search
import requests
import os
from dotenv import load_dotenv, find_dotenv
from requests.structures import CaseInsensitiveDict

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

SHEETS_ENDPOINT = os.getenv('SHEETS_ENDPOINT')

flight_search = flight_search.FlightSearch()
# class DataManager:
#     #This class is responsible for talking to the Google Sheet.
#     def put_data(self, data, row : int , column : str):
#         new_data = {
#             "price": {
#                 column: data
#                 }
#             }
#         response = requests.put(SHEETS_ENDPOINT+f"/{row}", data=new_data)
#         return response

#     @staticmethod
#     def fill_iata_codes(self):

def put_data(data, row : int , column : str):
    headers = CaseInsensitiveDict()
    headers["Content-Type"] = "application/json"
    # headers["Authorization"] = "Bearer your_token"
    endpoint = f"{self.endpoint}/{row_id}"
    response = requests.put(endpoint, headers=headers, json=data)
    response.raise_for_status()


sheet_response = requests.get(SHEETS_ENDPOINT)
# print(SHEETS_ENDPOINT)
# print(response.json())
num_of_cities = len(sheet_response.json()['prices'])
# print(num_of_cities)
for i in range(num_of_cities):
    # print(i)
    city = sheet_response.json()['prices'][i]['city']
    # print(city)
    # print(type(response.json()['prices'][i]['iataCode']))
    if sheet_response.json()['prices'][i]['iataCode'] == "":
        iata_code = flight_search.get_iata_code(city)
        # print(iata_code)
        response = put_data(iata_code, i+1, 'iataCode')
        print(response.status_code)
        pass
    else:
        pass
        pass
    
