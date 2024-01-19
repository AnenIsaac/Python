# class FlightSearch:
#     #This class is responsible for talking to the Flight Search API.
#     pass

import requests
from requests.structures import CaseInsensitiveDict
from flight_data import FlightData

class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.endpoint = "https://tequila-api.kiwi.com"
        self.api_key = "your_api_key"

    def get_destination_code(self, city_name):
        headers = CaseInsensitiveDict()
        headers["Accept"] = "application/json"
        endpoint = f"{self.endpoint}/locations/query"
        params = {
            "term": city_name,
            "location_types": "city",
            "active_only": "true",
            "sort": "name",
            "limit": "1"
        }
        response = requests.get(endpoint, headers=headers, params=params)
        response.raise_for_status()
        return response.json()["locations"][0]["code"]

    def search_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        headers = CaseInsensitiveDict()
        headers["Accept"] = "application/json"
        headers["apikey"] = self.api_key
        endpoint = f"{self.endpoint}/v2/search"
        params = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "USD"
        }
        response = requests.get(endpoint, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()["data"][0]
        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport_code=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport_code=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )
        return flight_data
