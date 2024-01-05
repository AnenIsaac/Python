from datetime import datetime 
import smtplib
import requests
from config import *

time_now = datetime.now()
MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude

def ISS_above(MY_LAT, MY_LONG, iss_latitude, iss_longitude):
    """Function to check if the ISS is withing 5 coordinates of my location (visible)"""
    if iss_latitude > MY_LAT:
        lat_diff = iss_latitude - MY_LAT
    elif MY_LAT > iss_latitude:
        lat_diff = MY_LAT - iss_latitude
    if iss_longitude > MY_LONG:
        long_diff = iss_longitude - MY_LONG
    elif MY_LONG > iss_longitude:
        long_diff = MY_LONG - iss_longitude
        
    # and it is currently dark
    if lat_diff < 5 and long_diff < 5 and is_dark():
        return True
    else:
        return False
    

def send_email(email : str):
    """Send email that the ISS is above you"""
    MY_EMAIL = "kelvinisshayo@gmail.com"
    PASSWORD = "macmuykehevhutvh"
    with smtplib.SMTP("smtp.gmail.com", port=587,) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, PASSWORD)
        connection.sendmail(MY_EMAIL, to_addrs=email, msg=f"Subject: The ISS is above you!\n\nLook up now to see the ISS right above you.")
        

def is_dark():
    """Check if it is dark at your location"""
    parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour()

    if time_now >= sunset or time_now <= sunrise:
        return True
    else:
        return False