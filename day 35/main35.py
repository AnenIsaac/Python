from twilio.rest import Client
import requests
import os

account_sid = 'AC9de5760c324ae7f89dab730976d99200'
auth_token = '6a0034540a919565d760677076a86f1c'

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall?"
api_key = "c08fb40de83eeb85b066a701a89055af"

weather_params = {
    "lat": 51.5073151,
    "lon": -0.127758, 
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
        
if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
    from_='+12056905776',
    body="Hey Anen, it seems like it might rain today. Make sure to bring an umbrella!",
    to='+255763860354'
    )



    
#print(hour_data["weather"][0]["id"])
#print(response.json())