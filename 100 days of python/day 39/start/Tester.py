import requests
import pandas as pd
from datetime import datetime, timedelta

sheet_endpoint = "https://api.sheety.co/db576b61a317675d114004c8294a6961/flightDeals/prices"
tequila_endpoint = "https://api.tequila.kiwi.com/"
search_endpoint = "v2/search"
locations_api = "locations/query"
tequila_header = {
    'apikey': '2Zc583pgrksLuGUf-3jTz9cuIu7nJI03'
}

# Get today's date
today = datetime.today()

# Calculate tomorrow's date by adding one day
first_day_departure = today + timedelta(days=1)
first_day_departure = first_day_departure.strftime('%d/%m/%Y')
last_day_departure = today + timedelta(days=180)
last_day_departure = last_day_departure.strftime('%d/%m/%Y')
first_day_return = today + timedelta(days=7)
first_day_return = first_day_return.strftime('%d/%m/%Y')
last_day_return = today + timedelta(days=210)
last_day_return = last_day_return.strftime('%d/%m/%Y')

# Fetch data from Sheety API
sheet_response = requests.get(sheet_endpoint).json()
print(sheet_response)

# Create DataFrame from the response
df = pd.DataFrame(sheet_response['prices'])
print(df)

for index, row in df.iterrows():
    city = row['iataCode']
    lowest_price = row['lowestPrice']
    print(city)
    print(lowest_price)
    search_params = {
    'fly_from': 'LON',
    'fly_to': city, 
    'date_from': first_day_departure, 
    'date_to': last_day_departure,
    'return_from': first_day_return,
    'return_to': last_day_return,
    'price_to': lowest_price
    }

    flight_response = requests.get(tequila_endpoint + search_endpoint, headers=tequila_header, params=search_params).json()
    print(flight_response['data'][0]['price'])
    









# # Iterate over cities in the DataFrame
# rowid = 2
# for city in df['city']:
#     tequilla_params = {
#         'term': city  # Use 'term' key to specify the city name
#     }
#     # Make Tequila API request
#     json_data = requests.get(tequila_endpoint + locations_api, params=tequilla_params, headers=tequila_header).json()
#     iata_code =json_data['locations'][0]['code']  # Corrected to access the 'locations' key
#     put_url = sheet_endpoint + "/" + str(rowid)  # Assuming 'objectId' is a valid column in your DataFrame
#     new_data = {
#                 "price": {
#                     "iataCode": iata_code
#                 }
#             }
#     response = requests.put(
#                 url=put_url,
#                 json=new_data
#             )
#     rowid+=1
    
    
    
