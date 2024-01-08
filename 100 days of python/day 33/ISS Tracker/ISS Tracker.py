import requests
from datetime import datetime
import smtplib
from config import *
MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])
    
#If the ISS is close to my current position

# Then send me an email to tell me to look up.
if ISS_above(MY_LAT, MY_LONG, iss_longitude, iss_latitude):
    send_email("anenbisaaclaseko@gmail.com")
else: 
    print("you can't see the space station right now!")
    
# BONUS: run the code every 60 seconds.



