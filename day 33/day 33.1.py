import requests

MY_LAT = 6.8165
MY_LONG = 39.2894
# response = requests.get(url="http://api.open-notify.org/iss-now.json")

#Trying to raise an exception for every single error code
# if response.status_code == 404:
#     raise Exception("That resource doesn't exist!")
# elif response.status_code == 401:
#     raise Exception("You are not authourized to access this resource!")


#Using the request module to raise exceptions
# response.raise_for_status()

# data = response.json()
# iss_position = (data["iss_position"]["latitude"], data["iss_position"]["longitude"])
# print(iss_position)
parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}
response = requests.get(url=f"https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
# print(data)


sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

print(int(sunrise)+3)
print(int(sunset)+3)